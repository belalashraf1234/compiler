from tokens import *
from model import *


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
            print(f'found {self.previous_token().lexeme} at the end of line pasing')
        elif self.peak().type==type:
            token= self.advance()
            return token
        else:
            raise SyntaxError(f"Expected token of type {type}, but found {self.peek().type} with lexeme '{self.peek().lexeme}' at line {self.peek().line}")
        


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
            return Intger(int(self.previous_token().lexeme))
        if self.match(TOK_FLOAT):
            return Float(float(self.previous_token().lexeme))
        if self.match(TOK_LPAREN):
            expr = self.expr()
            if not (self.match(TOK_RPAREN)):
                raise SyntaxError("Expected ')'")
            else:
                return Grouping(expr)
        if self.curr >= len(self.tokens):
            raise SyntaxError("Unexpected end of input")
        raise SyntaxError(f"Unexpected token: {self.peek().lexeme}")
       
    def unary(self):
        if self.match(TOK_NOT) or self.match(TOK_MINUS) or self.match(TOK_PLUS):
            op = self.previous_token()
            operand = self.unary()
            return UnOp(op, operand)
        return self.primary()
    def factor(self):
       return self.unary()
    def term(self):
        expr= self.factor()
        while self.match(TOK_STAR) or self.match(TOK_SLASH):
            op = self.previous_token()
            right = self.factor()
            expr = BinOp(op, expr, right)
        return expr
    def expr(self):
        expr=self.term()
        while self.match(TOK_PLUS) or self.match(TOK_MINUS):
            op=self.previous_token()
            right=self.term()
            expr=BinOp(op, expr, right)
        return expr


    def parse(self):
        ast=self.expr()
        return ast