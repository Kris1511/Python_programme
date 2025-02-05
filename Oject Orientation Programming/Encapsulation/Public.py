
# Public:
# The variable which are public, can be accessed inside the same class, outside of any class, inside the child class, 
# inside non-child class.


class Demo1:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

d1 = Demo1("Raj")
print(d1.name)
d1.display()

class Demo2(Demo1):
    def display2(self):
        print(self.name)

d2 = Demo2("Ak")
print(d2.name)
d2.display2()