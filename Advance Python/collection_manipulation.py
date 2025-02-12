li = [2, 5, 8, 4, 9]

# map function(function, iterable_object)
def double(num):
    return num * 2

double_li = list(map(double, li))
print(double_li)                        # [4, 10, 16, 8, 18]


# filter function(function, iterable_object)
def checkEven(num):
    return num % 2 == 0

evenNum = list(filter(checkEven, li))
print(evenNum)                          # [2, 8, 4]


# reduce    first import the package

from functools import reduce

def mul(a, b):
    return a * b            # here first come 2 * 5 = 10 and store in a = 10, b = 8  and store in a = 80, b = 4 and store in a = 160, b = 9 and store in 1440 like this 

result = reduce(mul, li)
print(result)                   # 2880
