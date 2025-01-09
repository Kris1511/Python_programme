# important key points:
# 1. Typecasting is the process of converting the data from one type to another type.
# 1. while converting int to bool for all non-zero values it will return True.
# 2. while converting int to bool for 0 it will return False.

# string is converted into integer using int() function.
a = '30'
print(a, type(a))
b = int(a)
print(b, type(b))


#  string to integer conversion not allowed if string contains alphabets
c = 'Kod'
print(c, type(c))
# y = int(c)
# print(y, type(y))    # ValueError: invalid literal for int() with base 10: 'Kod'

# float conversion
d = float(input('Enter a number: '))
print(d, type(d))

# boolean conversion
e = 12              # give -12 get true
print(e, type(e))   # 12 <class 'int'>
q = bool(e)
print(q, type(q))   # True <class 'bool'>

#Bool
f = ""
print(f, type(f))   # empty string <class 'str'>
g = bool(f)
print(g, type(g))   # False <class 'bool'>