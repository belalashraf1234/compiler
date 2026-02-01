from tokens import *
class Node:
    pass
class Expression(Node):
   pass




class Decl(Stmt):
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
    def __init__(self,val,end,line):
        assert isinstance(val,Expression),val
        self.value=val
        self.end=end
        self.line=line
    def __repr__(self):
        return f'PrintStmt({self.value}), end={self.end!r}'
class WhileStmt(Stmt):
    def __init__(self,test,body_stmts,line):
        assert isinstance(test,Expression),test
        assert isinstance(body_stmts,Stmts),body_stmts
        self.test=test
        self.body_stmts=body_stmts
        self.line=line
    def __repr__(self):
        return f'WhileStmt({self.test},{self.body_stmts})'
    
class Assignment(Stmt):
    def __init__(self,left,right,line):
        assert isinstance(left,Expression),left
        assert isinstance(right,Expression),right
        self.left=left
        self.right=right
        self.line=line
    def __repr__(self):
        return f'Assiment({self.left}, {self.right})'
        
    
class IfStmt(Stmt):
    def __init__(self,test,then_stmts,else_stmts,line):
        assert  isinstance(test,Expression), test
        assert  isinstance(then_stmts,Stmts), then_stmts
        assert else_stmts is None or isinstance(else_stmts,Stmts), else_stmts
        self.test=test
        self.then_stmts=then_stmts
        self.else_stmts=else_stmts
        self.line=line
    def __repr__(self):
        return f'IfStmt({self.test}, true:{self.then_stmts}, else:{self.else_stmts}'

class Identifier(Expression):
    def __init__(self,name,line):
        assert isinstance(name,str),name
        self.name=name
        self.line=line
        
    def __repr__(self):
        return f'Identifier({self.name})'

class ForStmt(Stmt):
    def __init__(self,ident,start,end,step,body_stmts,line):
        assert isinstance(ident,Identifier),ident
        assert isinstance(start,Expression),start
        assert isinstance(end,Expression),end
        assert isinstance(step,Expression) or step is None,step
        assert isinstance(body_stmts,Stmts),body_stmts
        self.ident=ident
        self.start=start
        self.end=end
        self.step=step
        self.body_stmts=body_stmts
        self.line=line
    def __repr__(self):
        return f'ForStmt({self.ident},{self.start},{self.end},{self.step},{self.body_stmts})'



class FuncDecl(Decl):
    def __init__(self,name,params,body_stmts,line):
        assert isinstance(name,str),name
        assert all(isinstance(param,Params) for param in params)
        self.name=name
        self.params=params
        self.body_stmts=body_stmts
        self.line=line
    def  __repr__(self):
        return f'FuncDecl({self.name!r}, {self.params}, {self.body_stmts})'
 
    

class Params(Decl):
    def __init__(self,name,line):
        assert isinstance(name,str),name
        self.name=name
        self.line=line
    def __repr__(self):
        return f'Param[{self.name!r}]'
     

class FuncCall(Expression):
     def __init__(self,name,args,line):
      
        self.name=name
        self.args=args
        self.args=args
        self.line=line
     def  __repr__(self):
        return f'FuncDecl({self.name!r}, {self.args})'
