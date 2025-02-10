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