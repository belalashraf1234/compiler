import sys
from tokens import *
from lexer import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <source_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    
    with open(source_file, 'r') as file:
        source_code = file.read()
        tokens = Lexer(source_code).tokenize()
        for token in tokens:
            print(token)
        
      