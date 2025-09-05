from model import *

class Interpreter:
    def __init__(self):
        pass
    def interpret(self,node):
        if isinstance(node,Intger):
            return float(node.value)
        elif isinstance(node,Float):
            return float(node.value)
        elif isinstance(node,Grouping):
            return self.interpret(node.expression)
        
        elif isinstance(node,BinOp):
            left=self.interpret(node.left)
            right=self.interpret(node.right)
            if node.operator.type==TOK_PLUS:
                return left+right
            elif node.operator.type==TOK_MINUS:
                return left-right
            elif node.operator.type==TOK_STAR:
                return left*right
            elif node.operator.type==TOK_SLASH:
                return left/right
        
        elif isinstance(node,UnOp):
            operand=self.interpret(node.operand)
            if node.operator.type==TOK_PLUS:
                return +operand
            elif node.operator.type==TOK_MINUS:
                return -operand





