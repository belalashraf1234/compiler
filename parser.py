from tokens import *
from model import *
from utils import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.curr = 0
    def advance(self):
       token= self.tokens[self.curr]
       self.curr += 1
       return token
    def peek(self):
        return self.tokens[self.curr]
    
    def previous_token(self):
        return self.tokens[self.curr - 1]
    
    def is_next(self, type):
        if self.curr >= len(self.tokens):
            return False
        return self.peek().type == type
        
    def expect(self, type):
        if self.curr >= len(self.tokens):
            parse_error(f'found {self.previous_token().lexeme} at the end of line pasing',self.previous_token.line)
        elif self.peak().type==type:
            token= self.advance()
            return token
        else:
            parse_error(f"Expected token of type {type}, but found {self.peek().type} with lexeme '{self.peek().lexeme}' ",self.peek().line)
        


    def match(self,type):
        if self.curr >= len(self.tokens):
            return False
        if self.peek().type!= type:
            return False
        self.curr += 1
        return True

      
    
    def grouping(self):
        pass
    def primary(self):
        if self.match(TOK_INTEGER):
            return Intger(int(self.previous_token().lexeme),line=self.previous_token().line)
        if self.match(TOK_FLOAT):
            return Float(float(self.previous_token().lexeme), line=self.previous_token().line)
        if self.match(TOK_TRUE):
            return Bool(True,line=self.previous_token().line)
        if self.match(TOK_FALSE):
            return Bool(False,line=self.previous_token().line)
        if self.match(TOK_STRING):
            return String(str(self.previous_token().lexeme[1:-1]),line=self.previous_token().line)
        if self.match(TOK_LPAREN):
            expr = self.expr()
            if not (self.match(TOK_RPAREN)):
               parse_error("Expected ')'",self.previous_token().line)
            else:
                return Grouping(expr,line=self.previous_token().line)
        if self.curr >= len(self.tokens):
            parse_error("Unexpected end of input",self.previous_token().line)
        parse_error(f"Unexpected token: {self.peek().lexeme}",self.peek().line)
       
    def unary(self):
        if self.match(TOK_NOT) or self.match(TOK_MINUS) or self.match(TOK_PLUS):
            op = self.previous_token()
            operand = self.unary()
            return UnOp(op, operand,self.previous_token().line)
        return self.primary()
    
    
    def multiplication(self):
        expr= self.unary()
        while self.match(TOK_STAR) or self.match(TOK_SLASH):
            op = self.previous_token()
            right = self.unary()
            expr = BinOp(op, expr, right,self.previous_token().line)
        return expr
    def addition(self):
        expr=self.multiplication()
        while self.match(TOK_PLUS) or self.match(TOK_MINUS):
            op=self.previous_token()
            right=self.multiplication()
            expr=BinOp(op, expr, right,self.previous_token().line)
        return expr


    def expr(self):
        return self.addition()
        