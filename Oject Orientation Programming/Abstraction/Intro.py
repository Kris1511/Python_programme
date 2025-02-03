from abc import ABC, abstractmethod

# Abstract class does not have any method then object for that abstract class is created.

class Demo1(ABC):
    @abstractmethod
    def display(self):
        pass

# Demo1()         # <__main__.Demo1 object at 0x0000021D3D3D3A00>

# Abstract class have any method then object for that abstract class is created.

class Demo2(ABC):

    def show(self):
        print("I am from Demo2 class")

Demo2().show()          # I am from Demo2 class


class Demo3(ABC):
    def info(self):
        print("I am from Demo3 class")

    @abstractmethod
    def display(self):
        pass

class Demo4(Demo3):
    pass

d4 = Demo4()    
d4.info()               # I am from Demo3 class
