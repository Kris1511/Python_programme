'''
1. In tuple we can store homogeneous as well as heterogeneous data.
2. In tuple we can store duplicate data.
3. tuple is an ordered collection of data: order of insertion will remain as it is in the output.
4. tuple is immutable: we can't change the data.  
'''

tup1 = (10, 20, 44.39, 'Kodnest', True, 20)
print(tup1)             # (10, 20, 44.39, 'Kodnest', True, 20)

# tup1.append(300) show error we can't change the data.

# tup1.remove(20) show error we can't remove the data.

# del tup1[2] show error we can't delete the data.

print(tup1[2])          # 44.39

# del tup1            # delete complete object
# print(tup1) we can't access the tup1 it's already deleted

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)               # (1, 2, 3, 4, 5, 6)