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
        elif self.peek().type==type:
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
        elif self.match(TOK_FLOAT):
            return Float(float(self.previous_token().lexeme), line=self.previous_token().line)
        elif self.match(TOK_TRUE):
            return Bool(True,line=self.previous_token().line)
        elif self.match(TOK_FALSE):
            return Bool(False,line=self.previous_token().line)
        elif self.match(TOK_STRING):
            return String(str(self.previous_token().lexeme[1:-1]),line=self.previous_token().line)
        elif self.match(TOK_LPAREN):
            expr = self.expr()
            if not (self.match(TOK_RPAREN)):
               parse_error("Expected ')'",self.previous_token().line)
            else:
                return Grouping(expr,line=self.previous_token().line)
        else:
            identifier=self.expect(TOK_IDENTIFIER)
            return Identifier(identifier.lexeme,line=self.previous_token().line)
        if self.curr >= len(self.tokens):
            parse_error("Unexpected end of input",self.previous_token().line)
        parse_error(f"Unexpected token: {self.peek().lexeme}",self.peek().line)
    
    def exponent(self):
        expr=self.primary()
        if self.match(TOK_CARET):
            op = self.previous_token()
            right = self.exponent()
            expr=BinOp(op,expr,right,line=op.line)
        return expr        
   
    def unary(self):
        if self.match(TOK_NOT) or self.match(TOK_MINUS) or self.match(TOK_PLUS):
            op = self.previous_token()
            operand = self.unary()
            return UnOp(op, operand,line=op.line)
        return self.exponent()
    
    
    
    def module(self):
        expr=self.unary()
        if self.match(TOK_MOD):
            op = self.previous_token()
            right = self.unary()
            expr=BinOp(op,expr,right,line=op.line)
        return expr
    
    def multiplication(self):
        expr= self.module()
        while self.match(TOK_STAR) or self.match(TOK_SLASH):
            op = self.previous_token()
            right = self.module()
            expr = BinOp(op, expr, right,line=op.line)
        return expr
    def addition(self):
        expr=self.multiplication()
        while self.match(TOK_PLUS) or self.match(TOK_MINUS):
            op=self.previous_token()
            right=self.multiplication()
            expr=BinOp(op, expr, right,line=op.line)
        return expr

    def comparison(self):
        expr=self.addition()
        while self.match(TOK_GT) or self.match(TOK_GE) or self.match(TOK_LT) or self.match(TOK_LE):
            op=self.previous_token()
            right=self.addition()
            expr=BinOp(op,expr,right,line=op.line)
        return expr
         

    def equality(self):
        expr=self.comparison()
        while self.match(TOK_NE) or self.match(TOK_EQEQ):
            op=self.previous_token()
            right=self.comparison()
            expr=BinOp(op,expr,right,line=op.line)
        return expr
    
    def logical_and(self):
        expr=self.equality()
        while self.match(TOK_AND):
            op=self.previous_token()
            right=self.equality()
            expr=LogicalOp(op,expr,right,line=op.line)
        return expr
    
    def logical_or(self):
        expr=self.logical_and()
        while self.match(TOK_AND):
            op=self.previous_token()
            right=self.logical_and()
            expr=LogicalOp(op,expr,right,line=op.line)
        return expr
    def expr(self):
        expr=self.logical_or()
        return expr
    
    def print_stmt(self,end):
        if self.match(TOK_PRINT) or self.match(TOK_PRINTLN):
            val=self.expr()
            return PrintStmt(val,end,line=self.previous_token().line)
    def if_stmt(self):
        self.expect(TOK_IF)
        test=self.expr()
        self.expect(TOK_THEN)
        then_stmts=self.stmts()
        if self.is_next(TOK_ELSE):
            self.advance()
            else_stmts=self.stmts()
        else:
            else_stmts=None
        self.expect(TOK_END)
        return IfStmt(test,then_stmts,else_stmts,line=self.previous_token().line)    





    def stmt(self):
        if self.peek().type == TOK_PRINT:
            return self.print_stmt(end='')
        if self.peek().type == TOK_PRINTLN:
            return self.print_stmt(end='\n')
        if self.peek().type == TOK_IF:
            return self.if_stmt()
        else:
            left=self.expr()
            if self.match(TOK_ASSIGN):
                right=self.expr()
                return Assignment(left,right,self.previous_token().line)
            else:
                pass

        


    def stmts(self):
        stmts=[]
        while self.curr<len(self.tokens) and not self.is_next(TOK_ELSE) and not self.is_next(TOK_END):            
            stmt=self.stmt()
            stmts.append(stmt)
        return Stmts(stmts,line=self.previous_token().line)    

    def program(self):
        stmts=self.stmts()
        return stmts

    def parse(self):
        ast=self.program()
        return ast
        