import sys
from tokens import *
from lexer import *
from parser import *
from utils import *
from interpreter import *
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <source_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    
    with open(source_file, 'r') as file:

        source_code = file.read()
        print(f'{Colors.GREEN}**************************************************{Colors.WHITE}')
print(f'{Colors.GREEN}SOURCE:{Colors.WHITE}')
print(f'{Colors.GREEN}**************************************************{Colors.WHITE}')
print(source_code)

print(f'{Colors.GREEN}**************************************************{Colors.WHITE}')
print(f'{Colors.GREEN}TOKENS:{Colors.WHITE}')
print(f'{Colors.GREEN}**************************************************{Colors.WHITE}')
tokens = Lexer(source_code).tokenize()
for tok in tokens:
    print(tok)

print()
print(f'{Colors.GREEN}**************************************************{Colors.WHITE}')
print(f'{Colors.GREEN}AST:{Colors.WHITE}')
print(f'{Colors.GREEN}**************************************************{Colors.WHITE}')
ast = Parser(tokens).parse()
print_pretty_ast(ast)
print()
print(f'{Colors.GREEN}**************************************************{Colors.WHITE}')
print(f'{Colors.GREEN}AST:{Colors.WHITE}')
print(f'{Colors.GREEN}**************************************************{Colors.WHITE}')
interpreter=Interpreter()
interpreter.interpret(ast)



