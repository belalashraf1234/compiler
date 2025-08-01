TOK_LPAREN      = 'TOK_LPAREN'      # (
TOK_RPAREN      = 'TOK_RPAREN'      # )
TOK_LCURLY      = 'TOK_LCURLY'      # {
TOK_RCURLY      = 'TOK_RCURLY'      # }
TOK_LSQUAR      = 'TOK_LSQUAR'      # [
TOK_RSQUAR      = 'TOK_RSQUAR'      # ]
TOK_COMMA       = 'TOK_COMMA'       # ,
TOK_DOT         = 'TOK_DOT'         # .
TOK_PLUS        = 'TOK_PLUS'        # +
TOK_MINUS       = 'TOK_MINUS'       # -
TOK_STAR        = 'TOK_STAR'        # *
TOK_SLASH       = 'TOK_SLASH'       # /
TOK_MOD         = 'TOK_MOD'         # %
TOK_CARET       = 'TOK_CARET'       # ^
TOK_COLON       = 'TOK_COLON'       # :
TOK_SEMICOLON   = 'TOK_SEMICOLON'   # ;
TOK_QUESTION    = 'TOK_QUESTION'    # ?
TOK_NOT         = 'TOK_NOT'         # !
TOK_GT          = 'TOK_GT'          # >
TOK_LT          = 'TOK_LT'          # <

# Two-char tokens
TOK_GE          = 'TOK_GE'          # >=
TOK_LE          = 'TOK_LE'          # <=
TOK_NE          = 'TOK_NE'          # !=
TOK_EQ          = 'TOK_EQ'          # ==
TOK_ASSIGN      = 'TOK_ASSIGN'      # =
TOK_GGT         = 'TOK_GGT'         # >>
TOK_LLT         = 'TOK_LLT'         # <<

# Literals
TOK_IDENTIFIER  = 'TOK_IDENTIFIER'
TOK_STRING      = 'TOK_STRING'
TOK_INTEGER     = 'TOK_INTEGER'
TOK_FLOAT       = 'TOK_FLOAT'

# Keywords
TOK_IF          = 'TOK_IF'
TOK_THEN        = 'TOK_THEN'
TOK_ELSE        = 'TOK_ELSE'

class Token:
    def __init__(self, type, source, line, column):
        self.type = type
        self.source = source
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {self.source}, {self.line})"