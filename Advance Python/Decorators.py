def decor(func):
    def inner(name):
        if name == "Ayush":
            print(name, 'is learning java')
        else:
            func(name)

    return inner

@decor
def choice(name):
    print(name, ' is learning python')

choice("Ayush")
choice("Akash")


# ex: 1 

def smart(func):
    def inner(a, b):
        if b == 0:
            print(f'b should not be 0')
        else:
            func(a, b)
    return inner

@smart
def div(a, b):
    print(f'Division: ', a / b)

div(10, 5)              # 2.0
div(42, 7)              # 6.0

# ex: 2

def repeat(num):
    def outer(func):
        def inner():
            for i in range(num):
                func()
        return inner
    return outer
    

@repeat(num = 3)
def msg():
    print('Hello')

msg()       # this one print 3 times hello
msg()       # this one print 3 times hello