# list iterable object are:
# 1. list
# 2. set
# 3. tuple
# 4. range
# 5. dict - only keys

li1 = list('Kod')           # ['K', 'o', 'd'] only string not int, float
print(li1)

li2 = list((10, 20))
print(li2)                  # [10, 20]

li3 = list({100, 200})
print(li3)                  # [200, 100]

li4 = list({'Name': 'arun', 'age' : 29})
print(li4)                  # ['Name', 'age']

li5 = list(range(2, 10))
print(li5)                  # [2, 3, 4, 5, 6, 7, 8, 9]



# tuple iterable object:
tup1 = tuple([10, 20, 30])
print(tup1)         # (10, 20, 30)

tup2 = tuple({100, 300, 440})
print(tup2)         # (440, 100, 300)

tup3 = tuple(range(1, 10))
print(tup3)         # (1, 2, 3, 4, 5, 6, 7, 8, 9)

tup4 = tuple('Kodnest')
print(tup4)         # ('K', 'o', 'd', 'n', 'e', 's', 't')

tup5 = tuple({'name' : 'basha', 'age' : 30})
print(tup5)         # ('name', 'age')


# set iterable object
s1 = set([10, 20, 30])
print(s1)           # {10, 20, 30}


# dict iterable object
