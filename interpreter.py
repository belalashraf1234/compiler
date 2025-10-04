from model import *
from utils import *

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
            
                

        
        elif isinstance(node,UnOp):
            operandtype,operandval=self.interpret(node.operand)
            if node.operator.type==TOK_PLUS:
                if operandtype==TYPE_NUMBER:
                    return (TYPE_NUMBER,+operandval)
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





