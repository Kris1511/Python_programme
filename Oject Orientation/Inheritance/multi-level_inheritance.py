class Demo1():
    def display1(self):
        print('Inside Display1')

class Demo2(Demo1):
    def display2(self):
        print('Inside Display2')

class Demo3(Demo2):
    def display3(self):
        print('Inside Display3')    

d2 = Demo2()
d2.display1()  # Output: Inside Display1
d2.display2()  # Output: Inside Display2

d3 = Demo3()
d3.display1()  # Output: Inside Display1
d3.display2()  # Output: Inside Display2
d3.display3()  # Output: Inside Display3