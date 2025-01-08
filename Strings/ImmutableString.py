# 1. Strings are immutable in Python. Once we declare the string we can't modify it.
# if we try to modify it, it will create a new string object.

# 2. If new string does not have any reference variable then it will be removed by garbage collector.
s1 = 'Kodnest'
s1.upper()
print(s1)

s2 = 'kodNest'
s2 = s2.upper()
print(s2)

s3 = 'K'
print(s3, id(s3))   # address get change

s4 = 'Hello'
s5 = 'World'
print(s4, id(s4))
print(s5, id(s5))

print(s4[0])
print(s5[-1])

print('Id of H: ', id(s4[0]))   # address about particular string
print('Id of o: ',id(s5[-1]))  # address about particular string

print('Id of W: ', id(s5[0]))   
print('Id of o: ',id(s5[1]))

print('Id of l: ', id(s4[2]))
print('Id of l: ', id(s4[3]))
print('Id of l: ', id(s5[3]))