from tokens import *
class Node:
    pass
class Expression(Node):
   pass

class Intger(Expression):
    def __init__(self, value,line):
        assert isinstance(value,int), value
        self.value = value
        self.line = line
    def __repr__(self):
        return f"Intger({self.value})"
    
class Stmt(Node):
    pass

class Grouping(Expression):
    def __init__(self, value,line):
        assert isinstance(value, Expression), value
        self.expression = value
        self.line = line 
    def __repr__(self):
        return f"Grouping({self.expression})"

class Float(Expression):
    def __init__(self, value,line):
        assert isinstance(value,float), value
        self.value = value
        self.line = line
    def __repr__(self):
        return f"Float({self.value})"
class UnOp(Expression):
    def __init__(self, operator:Token, operand:Expression, line):
        
        assert isinstance(operand, Expression), operand
        assert isinstance(operator, Token), operator
        self.operand = operand
        self.operator = operator
        self.line = line
       

    def __repr__(self):
        return f"UnOp(, {self.operator.lexeme}, {self.operand})"
class BinOp(Expression):
    def __init__(self, operator:Token, left:Expression, right:Expression,line):
        assert isinstance(left, Expression), left
        assert isinstance(right, Expression), right
        assert isinstance(operator, Token), operator
        self.left = left
        self.operator = operator
        self.right = right
        self.line = line

    def __repr__(self):
        return f"BinOp({self.operator.lexeme}, {self.left},  {self.right})"

def WhileStmt(Stmt):
    pass
def Assignment(Stmt):
    pass
def IfStmt(Stmt):
    pass

def ForStmt(Stmt):
    pass
