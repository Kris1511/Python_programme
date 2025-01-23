# print('kodnest1234*'.isalnum())     # False

# print('kodnest1234'.isalnum())      # True

# print('kodnest1234*'.isalpha())     # False

# print('kodnest1234'.isalpha())     # False

# print('kodnest'.isalpha())     # True

# print('1234'.isdigit())     # True

# print('kodnest1234*'.isalpha())     # False

# print('kodnest'.islower())     # True

# print('kodnest'.isupper())     # False

# print(any((True, False, False)))     # True

# print(any((False, False, False)))     # True

# question 1

s = input()             # qA1

print(any([i.isalnum() for i in s]))        # True

print(any([i.isalpha() for i in s]))        # True

print(any([i.isdigit() for i in s]))        # True

print(any([i.islower() for i in s]))        # True

print(any([i.isupper() for i in s]))        # True
