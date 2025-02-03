# In python if we print reference variable then internally python will invoke the dundar method __str__() method which always 
# returns string representation of an address of the object.

# Dunder method:
# Dunder method is the method which starts and ends with double underscore.
# Dunder method is also called as magic method. we don't need to call these methods.
# automatically these methods will be called by python internally.


class Demo1:
    def display(self):
        print("I am from Demo1 class")

    def __str__(self):
        return "Demo1 class object"

    def __add__(self, other):
        self.a = 10
        other.b = 20
        return self.a + other.b

class Demo2:
    def display(self):
        print("I am from Demo2 class")

    def __str__(self):
        return "Demo2 class object"

    def __sub__(self, other):
        self.a = 10
        other.b = 5
        return self.a - other.b

d1 = Demo1()
d2 = Demo2()

print(d1)
print(d2)
print(d1 + d2)          # 30
print(d2 - d2)          # 5