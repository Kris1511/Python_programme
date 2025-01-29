class Calculator():
    def add():
        print()
        

class Add(Calculator):
    def add(self, a, b):
        print(a + b)

class Subtract(Calculator):
    def subtract(self, a, b):
        print(a - b)

def permit(ref, a, b):
    ref.calculate(a, b)
permit(Add(), 10, 20)
permit(Subtract(), 10, 20)