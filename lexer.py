from tokens import *
class Lexer:
    def __init__(self, source_code):
      self.tokens = []
      self.start= 0
      self.current = 0
      self.line = 1      
      self.source_code = source_code
    
    def advance(self):
       ch=self.source_code[self.current]
       self.current += 1
       return ch
    def peak(self):
       if self.current >= len(self.source_code):
           return '\0' 
       return self.source_code[self.current] # End of input
    def match(self, expected):
       if self.current>= len(self.source_code):
           return False
       if self.source_code[self.current] != expected:
           return False
       self.current=self.current + 1
       return True
    def look_ahead(self,n=1):
       if self.current + 1 >= len(self.source_code):
           return '\0'
       return self.source_code[self.current + n]
    def add_token(self, type):
     
       value = self.source_code[self.start:self.current]
       self.tokens.append(Token(type, value, self.line, self.start))
    def tokenize(self):
       while self.current < len(self.source_code):
           self.start = self.current
           char = self.advance()
           if char == '\n':
               self.line += 1
           elif char == ' ':
               pass
           elif char == '\t':
               pass
           elif char == '\r':
               pass
           elif char == '#':
               while self.peak() != '\n' and not(self.current >= len(self.source_code)):
                   self.advance()
               
           elif char == '(': self.add_token(TOK_LPAREN)
           elif char == ')': self.add_token(TOK_RPAREN)
           elif char == '{': self.add_token(TOK_LCURLY)
           elif char == '}': self.add_token(TOK_RCURLY)
           elif char == '[': self.add_token(TOK_LSQUAR)
           elif char == ']': self.add_token(TOK_RSQUAR)
           elif char == '.': self.add_token(TOK_DOT)
           elif char == ',': self.add_token(TOK_COMMA)
           elif char == '+': self.add_token(TOK_PLUS)
           elif char == '-': self.add_token(TOK_MINUS)
           elif char == '*': self.add_token(TOK_STAR)
           elif char == '/': self.add_token(TOK_SLASH)
           elif char == '%': self.add_token(TOK_MOD)
           elif char == '^': self.add_token(TOK_CARET)
           elif char == '?': self.add_token(TOK_QUESTION)
           elif char == ';': self.add_token(TOK_SEMICOLON)
           elif char=='=':
               self.add_token(TOK_EQ if self.match('=') else TOK_ASSIGN)
           elif char == '!':
               self.add_token(TOK_NE if self.match('=') else TOK_NOT)
           elif char == '>':
               self.add_token(TOK_GT if not self.match('=') else TOK_GE)
           elif char == '<':
               self.add_token(TOK_LT if not self.match('=') else TOK_LE)
           elif char == '>':
               self.add_token(TOK_GGT if self.match('>') else TOK_GT)
           elif char == '<':
               self.add_token(TOK_LLT if self.match('<') else TOK_LT)
           
          
       return self.tokens
       
        