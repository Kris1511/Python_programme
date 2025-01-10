# without input and without return type
def add():
    a = 10
    b = 20
    print('Addition is :',a + b)
add()

# with input and without return type
def sub(a, b):
    print('Subtraction is :',a - b)
sub(20, 10)

# without input and with return type   
def mul():
    a = 10
    b = 20
    return a * b
print('Multiplication is : ',mul())

# with input and with return type
def div(a, b):
    return a / b
print('Division is : ',div(20, 10))