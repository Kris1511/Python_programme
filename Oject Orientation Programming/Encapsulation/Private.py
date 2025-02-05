class Demo1:
    def __init__(self, name):
        self.__name = name

    def setName(self, name):
        return self.__name
        
    def getName(self):
        return self.__name

d1 = Demo1("Raj")
# print(d1.__name)        # AttributeError: 'Demo1' object has no attribute '__name'
# d1.display()            # Raj
# print(d1.display())     # Raj
print(d1.getName())     # Raj