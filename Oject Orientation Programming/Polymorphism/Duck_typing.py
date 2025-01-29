# Polymorphism is the ability of an object to take on many forms. 
# The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

class Add():
    def calc(self, a, b):
        print(a + b)

class Subtract():
    def calc(self, a, b):
        print(a - b)

class Multiply():
    pass

def permit(ref, a, b):
    if type(ref).__name__ == 'Multiply':
        print('Multiply class does not have calc() method')
    else:
        ref.calc(a, b)
    ref.calc(a, b)
permit(Add(), 10, 20)               # 30
permit(Subtract(), 20, 10)          # 10
# permit(Multiply(), 10, 20)          # Multiply class does not have calc() method 