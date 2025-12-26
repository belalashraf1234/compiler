from model import *
from utils import *
import codecs

TYPE_NUMBER='TYPE_NUMBER'
TYPE_STRING='TYPE_STRING'
TYPE_BOOL='TYPE_BOOL'
class Interpreter:
    def __init__(self):
        pass
    def interpret(self,node):
        if isinstance(node,Intger):
            return (TYPE_NUMBER,float(node.value))
        elif isinstance(node,Float):
            return (TYPE_NUMBER,float(node.value))
        elif isinstance(node,Bool):
            return (TYPE_BOOL,node.value)
        elif isinstance(node,String):
            return (TYPE_STRING,node.value)

        elif isinstance(node,Grouping):
            return self.interpret(node.expression)
        
        
        
        elif isinstance(node,BinOp):
            lefttype,leftval=self.interpret(node.left)
            righttype,rightval=self.interpret(node.right)

            if node.operator.type==TOK_PLUS:
                if lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER:
                    return (TYPE_NUMBER,leftval+rightval)
                elif lefttype==TYPE_STRING or righttype==TYPE_STRING:
                    return(TYPE_STRING,str(leftval)+str(rightval))
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line)
            elif node.operator.type==TOK_MINUS:
                if lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER:
                    return (TYPE_NUMBER,leftval-rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line)

            elif node.operator.type==TOK_STAR:
                if lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER:
                    return (TYPE_NUMBER,leftval*rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line)


            elif node.operator.type==TOK_SLASH:
                if rightval==0:
                    runtime_error(f'divison by zero',node.line)
                if lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER:
                    return (TYPE_NUMBER, leftval / rightval)

            elif node.operator.type==TOK_MOD:
                if lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER:
                    return (TYPE_NUMBER,leftval%rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line)
            elif node.operator.type==TOK_CARET:
                if lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER:
                    return (TYPE_NUMBER,leftval**rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line) 
            
            elif node.operator.type==TOK_GT:
                if(lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER) or (lefttype==TYPE_STRING and righttype==TYPE_STRING):
                    return(TYPE_BOOL,leftval>rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line)
            elif node.operator.type==TOK_GE:
                if(lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER) or (lefttype==TYPE_STRING and righttype==TYPE_STRING):
                    return(TYPE_BOOL,leftval>=rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line) 
            elif node.operator.type==TOK_GE:
                if(lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER) or (lefttype==TYPE_STRING and righttype==TYPE_STRING):
                    return(TYPE_BOOL,leftval>=rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line) 
          
            elif node.operator.type==TOK_LT:
                if(lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER) or (lefttype==TYPE_STRING and righttype==TYPE_STRING):
                    return(TYPE_BOOL,leftval<rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line) 
                
            elif node.operator.type==TOK_LE:
                if(lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER) or (lefttype==TYPE_STRING and righttype==TYPE_STRING):
                    return(TYPE_BOOL,leftval<=rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line)

            elif node.operator.type==TOK_EQEQ:
                if(lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER) or (lefttype==TYPE_STRING and righttype==TYPE_STRING) or (lefttype==TYPE_BOOL and righttype==TYPE_BOOL):
                    return(TYPE_BOOL,leftval==rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line)

            elif node.operator.type==TOK_NE:
                if(lefttype==TYPE_NUMBER and righttype==TYPE_NUMBER) or (lefttype==TYPE_STRING and righttype==TYPE_STRING) or (lefttype==TYPE_BOOL and righttype==TYPE_BOOL):
                    return(TYPE_BOOL,leftval!=rightval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} between {lefttype} and {righttype} ',node.operator.line)  

        
        elif isinstance(node,UnOp):
            operandtype,operandval=self.interpret(node.operand)
            if node.operator.type==TOK_PLUS:
                if operandtype==TYPE_NUMBER:
                    return (TYPE_NUMBER,operandval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} with {operandtype} ',node.operator.line) 
                
            elif node.operator.type==TOK_MINUS:
                if operandtype==TYPE_NUMBER:
                    return (TYPE_NUMBER,-operandval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} with {operandtype} ',node.operator.line) 

            elif node.operator.type==TOK_NOT:
                if operandtype==TYPE_BOOL:
                    return (TYPE_NUMBER,not operandval)
                else:
                    runtime_error(f'Unsupported operator {node.operator.lexeme!r} with {operandtype} ',node.operator.line) 

        elif isinstance(node,LogicalOp):
            lefttype,leftval=self.interpret(node.left)
            if node.operator.type==TOK_OR:
                if leftval:
                    return (lefttype,leftval)
            elif node.operator.type==TOK_AND:
                if not leftval:
                    return (lefttype,leftval)
            return self.interpret(node.right)
        
        elif isinstance(node,Stmts):
            for stmt in node.stmts:
                self.interpret(stmt)
        elif isinstance(node,PrintStmt):
            exprtype,exprval=self.interpret(node.value)
            print(codecs.escape_decode(bytes(str(exprval), "utf-8"))[0].decode("utf-8"),end=node.end)
        elif isinstance(node,IfStmt):
            testtype,testval=self.interpret(node.test)
            if testtype !=TYPE_BOOL:
                runtime_error("Condition test is not a boolean expression",node.line)
            if testval:
                self.interpret(node.then_stmts)
            else:
                self.interpret(node.else_stmts)                 



