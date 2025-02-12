def display():          # method will return only one value
    return 10
    return 20
    return 30

res = display()
print(res)          # 10

# yield keyword

def generator_fun():
    yield 1                 # pause ->print
    print('one')            # resume -> print including 3 also
    yield 3                 # pause
    yield 40                # resume -> print including 40 
    yield 23                # pause

res = generator_fun()
print(res)                  # return this only generator object <generator object generator_fun at 0x00000172B79F5B10>

print(next(res))            # 1
print(next(res))            # one
print(next(res))            # 3
print(next(res))            # 40

# normal fibonacci series
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        print(a)
        a, b = b, a + b

fibonacci(10)


# yield fibonacci 
def fibonacci_gen(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        a , b = b, a + b

ref = fibonacci_gen(1000)
print(f'fib1: ', next(ref))     # next means pause  fib1: 0
print(f'fib2: ', next(ref))     # resume            fib2: 1

for i in range(10):
    print(next(ref))            # 1 2 3 5 8 13 21 34 55 89