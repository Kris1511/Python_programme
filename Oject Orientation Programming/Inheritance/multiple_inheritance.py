class Demo1:
    def display1(self):
        print('Inside Display1')

class Demo2:
    def display2(self):
        print('Inside Display2')

class Demo3(Demo1, Demo2):
    def display3(self):
        print('Inside Display3')

d3 = Demo3()
d3.display1()        # Inside Display1
d3.display2()        # Inside Display2
d3.display3()        # Inside Display3

# what if have the same method in both the parent classes display() in Demo1 and display() in Demo2
# Method Resolution Order (MRO)
# d3.display()        # Inside Display3

# example 2

class A:
    def __init__(self):
        self.x = 100

class B:
    def __init__(self):
        self.x = 200

class C(A, B):
    def __init__(self):
        self.x = 300

d = C()
print(d.x)          # 300