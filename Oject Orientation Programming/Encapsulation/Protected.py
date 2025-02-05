# Protected:
# The variables which are protected, can be accessed inside the same class, outside any class, inside the child class, 


class Demo1:
    def __init__(self, name):
        self._name = name

    def display(self):
        print(self._name)

d1 = Demo1("Raj")
print(d1._name)
d1.display()

class Demo2(Demo1):
    def display(self):
        print(self._name)

d2 = Demo2("Ak")
print(d2._name)
print(d2._name)