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
class Bool(Expression):
    def __init__(self,value,line):
        assert isinstance(value,bool),value
        self.value=value
        self.line=line
    def __repr__(self):
        return f'Bool[{self.value}]'
        
    
class String(Expression):
    def __init__(self,value,line):
        assert isinstance(value,str),value
        self.value=value
        self.line=line
    def __repr__(self):
        return f'String[{self.value}]'
    
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


class LogicalOp(Expression):
    def __init__(self, operator:Token, left:Expression, right:Expression,line):
        assert isinstance(left, Expression), left
        assert isinstance(right, Expression), right
        assert isinstance(operator, Token), operator
        self.left = left
        self.operator = operator
        self.right = right
        self.line = line
    def __repr__(self):
        return f"LogicalOp({self.operator.lexeme}, {self.left},  {self.right})"

class Stmts(Node):
    def __init__(self,stmts,line):
        assert all(isinstance(stmt,Stmt)for stmt in stmts),stmts
        self.stmts=stmts
        self.line=line
    def __repr__(self):
        return f'Stmts ({self.stmts})'
class PrintStmt(Stmt):
    def __init__(self,val,line):
        assert isinstance(val,Expression),val
        self.value=val
        self.line=line
    def __repr__(self):
        return f'PrintStmt({self.value})'
class WhileStmt(Stmt):
    pass
class Assignment(Stmt):
    pass
class IfStmt(Stmt):
    pass

class ForStmt(Stmt):
    pass
