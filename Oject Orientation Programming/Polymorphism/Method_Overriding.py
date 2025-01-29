# In this code we achieve method overriding using inheritance.************
# We have a parent class Calculate with a method calc. 
# We have three child classes Add, Subtract and Multiply. 
# We have overridden the calc method in all the three child classes.

class Calculate():
    def calc(self, a, b):
        print(a * b)

class Add(Calculate):
    def calc(self, a, b):
        print("Addition: ", a + b)

class Subtract(Calculate):
    def calc(self, a, b):
        print("Subtraction: ", a - b)

class Multiply(Calculate):
    pass

ref = Add()
ref.calc(10, 20)               # 30

ref1 = Subtract()
ref1.calc(20, 10)              # 10

ref2 = Multiply()
ref2.calc(10, 20)              # 200 