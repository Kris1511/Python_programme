class Demo:
    def display(self):
        print('Inside Display')
        
    def display(self, name):
        print('Inside Display with name:', name)

    def display(self, name, age):
        print('Inside Display with name:', name, 'and age:', age)

    def display(self, name, age, city):
        print('Inside Display with name:', name, 'and age:', age, 'and city:', city)

d1 = Demo()
# d1.display()        
# d1.display('John')          
# d1.display('John', 25)
d1.display('John', 25, 'NY')        # Inside Display with name: John and age: 25 and city: NY