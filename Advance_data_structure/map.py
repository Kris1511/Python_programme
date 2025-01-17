# map is method. map method accept the 2 object
# syntax
# map(function, iterable_object) --> 

def double(x):
    return x * 2
li = [1, 2, 3, 4, 5]
li2 = list(map(double, li))
print(li2)          # [2, 4, 6, 8, 10]

tup = ('10', '20', '30')
print(tup)          # ('10', '20', '30')
tup1 = tuple(map(int, tup))
print(tup1)         # (10, 20, 30)

li3 = [1, 30, 48, 66]
print(li3)      # [1, 30, 48, 66]
floats = list(map(float, li3))
print(floats)       # [1.0, 30.0, 48.0, 66.0]
double_li = list(map(double, li3))
print(double_li)     # [2, 60, 96, 132]