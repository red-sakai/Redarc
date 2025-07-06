# nodes.py

class CallNode:
    def __init__(self, name, args):
        self.name = name
        self.args = args

class TimeBlockNode:
    def __init__(self, keyword, delay, body):
        self.keyword = keyword  # "every" or "after"
        self.delay = delay
        self.body = body  # list of CallNode

class LetNode:
    def __init__(self, name, value_expr):
        self.name = name
        self.value_expr = value_expr

class VarNode:
    def __init__(self, name):
        self.name = name

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
