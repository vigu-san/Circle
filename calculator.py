class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(a, b):
        return a+b
    def sub(a, b):
        return a-b
    def mul(a, b):
        return a*b
    def div(a, b):
        if b == 0:
            return "invalid"
        return a/b