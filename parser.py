# parser.py
from nodes import CallNode, TimeBlockNode, LetNode, VarNode, BinOpNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self, offset=0):
        if self.pos + offset < len(self.tokens):
            return self.tokens[self.pos + offset]
        return ('EOF', '')

    def match(self, kind):
        if self.peek()[0] == kind:
            self.pos += 1
            return True
        return False

    def consume(self, kind, error):
        if self.match(kind):
            return self.tokens[self.pos - 1][1]
        raise Exception(f"Parser error: {error}")

    def parse(self):
        nodes = []
        while self.peek()[0] != 'EOF':
            if self.peek()[0] == 'IDENT':
                if self.peek(1)[0] == 'LPAREN':
                    nodes.append(self.parse_call())
                else:
                    self.pos += 1
            elif self.peek()[0] in ('every', 'after'):
                nodes.append(self.parse_time_block())
            elif self.peek()[0] == 'let':
                nodes.append(self.parse_let())
            else:
                self.pos += 1
        return nodes

    def parse_call(self):
        name = self.consume('IDENT', "Expected function name")
        self.consume('LPAREN', "Expected (")
        args = []
        while self.peek()[0] != 'RPAREN':
            kind, value = self.peek()
            if kind == 'STRING':
                args.append(value.strip('"'))
            elif kind == 'NUMBER':
                args.append(float(value))
            elif kind == 'IDENT':
                args.append(value)
            self.pos += 1
            if self.peek()[0] == 'COMMA':
                self.pos += 1
        self.consume('RPAREN', "Expected )")
        return CallNode(name, args)

    def parse_time_block(self):
        keyword = self.consume(self.peek()[0], "Expected time keyword")
        self.consume('LPAREN', "Expected (")
        delay = float(self.consume('NUMBER', "Expected number"))
        self.consume('RPAREN', "Expected )")
        self.consume('COLON', "Expected :")

        body = []
        while self.peek()[0] == 'IDENT':
            body.append(self.parse_call())
        return TimeBlockNode(keyword, delay, body)

    def parse_let(self):
        self.consume('let', "Expected 'let'")
        name = self.consume('IDENT', "Expected variable name")
        self.consume('EQ', "Expected '='")
        expr = self.parse_expr()
        return LetNode(name, expr)

    def parse_expr(self):
        left = self.parse_term()
        while self.peek()[0] in ('PLUS', 'MINUS'):
            op = self.consume(self.peek()[0], "Expected operator")
            right = self.parse_term()
            left = BinOpNode(left, op, right)
        return left

    def parse_term(self):
        kind, value = self.peek()
        if kind == 'NUMBER':
            self.pos += 1
            return float(value)
        elif kind == 'IDENT':
            self.pos += 1
            return VarNode(value)
        elif kind == 'STRING':
            self.pos += 1
            return value.strip('"')
        else:
            raise Exception(f"Parser error: unexpected token {kind}")