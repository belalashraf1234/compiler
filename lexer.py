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
    def handle_identifier(self):
        while self.peak().isalnum() or self.peak() == '_':
            self.advance()
        text= self.source_code[self.start:self.current]
        keword_type=keywords.get(text)
        if keword_type == None:
            self.add_token(TOK_IDENTIFIER)
        else:
            self.add_token(keword_type)
       
    def handle_number(self):
        while self.peak().isdigit():
            self.advance()
        if self.peak() == '.' and self.look_ahead().isdigit():
            self.advance()
            while self.peak().isdigit():
                self.advance()
            self.add_token(TOK_FLOAT) 
        else:
            self.add_token(TOK_INTEGER)
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
    def handle_string(self,start_qoute):
        while self.peak() != start_qoute and not(self.current >= len(self.source_code)):
            self.advance()
        if self.current >= len(self.source_code):
            raise Exception(f"Unterminated string at line {self.line}")
        self.advance()  # Consume the closing quote
        self.add_token(TOK_STRING)
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
           elif char == ':':
               self.add_token(TOK_ASSIGN if self.match('=') else TOK_COLON)
           elif char=='=':
               self.add_token(TOK_EQEQ if self.match('=') else TOK_EQ)

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
           elif char.isdigit():
               self.handle_number()
           elif char=='"' or char=='\'':
               self.handle_string(char)
           elif char.isalpha() or char == '_':
               self.handle_identifier()
            
           
          
       return self.tokens
       
        