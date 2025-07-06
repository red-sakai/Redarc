from nodes import CallNode, TimeBlockNode, LetNode, VarNode, BinOpNode
from core.time import wait, now, schedule_every, schedule_after

class Interpreter:
    def __init__(self, nodes):
        self.nodes = nodes
        self.env = {}  # variable environment

    def run(self):
        for node in self.nodes:
            if isinstance(node, CallNode):
                self.eval_call(node)
            elif isinstance(node, TimeBlockNode):
                self.eval_time_block(node)
            elif isinstance(node, LetNode):
                value = self.eval_expr(node.value_expr)
                self.env[node.name] = value

    def eval_call(self, node):
        args = [self.eval_expr(arg) if isinstance(arg, (VarNode, BinOpNode)) else arg for arg in node.args]

        if node.name == "print":
            print(*args)
        elif node.name == "wait":
            wait(args[0])
        elif node.name == "now":
            print(now())
        else:
            print(f"[Runtime] Unknown function: {node.name}")

    def eval_time_block(self, node):
        if node.keyword == "every":
            schedule_every(node.delay, lambda: self.run_block(node.body))
        elif node.keyword == "after":
            schedule_after(node.delay, lambda: self.run_block(node.body))

    def run_block(self, block_nodes):
        for stmt in block_nodes:
            self.eval_call(stmt)

    def eval_expr(self, expr):
        if isinstance(expr, VarNode):
            return self.env.get(expr.name, f"[undefined {expr.name}]")
        elif isinstance(expr, BinOpNode):
            left = self.eval_expr(expr.left)
            right = self.eval_expr(expr.right)
            if expr.op == 'PLUS':
                return left + right
            elif expr.op == 'MINUS':
                return left - right
        elif isinstance(expr, (int, float, str)):
            return expr
        else:
            return expr  # already a value

if __name__ == "__main__":
    import sys
    from lexer import tokenize
    from parser import Parser

    # Use filename from command line or default to example.red
    filename = sys.argv[1] if len(sys.argv) > 1 else "example.red"

    with open(filename) as f:
        code = f.read()
    tokens = tokenize(code)
    nodes = Parser(tokens).parse()
    interpreter = Interpreter(nodes)
    interpreter.run()

    # Keep the main thread alive to allow scheduled events to run
    import time
    while True:
        time.sleep(1)
