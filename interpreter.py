from nodes import CallNode, TimeBlockNode, LetNode, VarNode, BinOpNode
from core.time import wait, now, schedule_every, schedule_after

class Interpreter:
    def __init__(self, nodes):
        self.nodes = nodes
        self.env = {}  # Variable environment

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
            return expr
