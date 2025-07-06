# lexer.py
import re

TOKEN_TYPES = [
    ('NUMBER', r'\d+(\.\d+)?'),
    ('STRING', r'"[^"]*"'),
    ('IDENT', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('COLON', r':'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('COMMA', r','),
    ('EQ', r'='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('STAR', r'\*'),
    ('SLASH', r'/'),
]

KEYWORDS = {'every', 'after', 'let'}

token_re = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)

def tokenize(code):
    tokens = []
    for match in re.finditer(token_re, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            continue
        if kind == 'IDENT' and value in KEYWORDS:
            kind = value
        tokens.append((kind, value))
    return tokens
