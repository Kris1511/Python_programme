# when we create multiple constructor in same class then only last constructor will be invoked at the time of 
# object creation. This is called constructor overloading.

class Demo:
    def __init__(self):
        self.x = 100

    def __init__(self):
        self.x = 200

    def __init__(self):
        self.x = 300

d = Demo()
print(d.x)              # 300