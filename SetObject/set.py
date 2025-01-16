'''
1. Inset we can store homogeneous as well as heterogeneous data.
2. set is unordered collection of data.
3. set does not support indexing of data.
4. In set we cannot store duplicate.
5. sets are mutable.
'''


s1 = { 10, True, 'Kodnest', 10, 20, 44.89 }

print(s1, type(s1))             # {True, 20, 'Kodnest', 10, 44.89} <class 'set'>

# print(s1[0])            # error bcz set does not support indexing of data.

# in set add only not append
# add
s1.add(400)
print(s1)               # {'Kodnest', True, 400, 20, 10, 44.89}

# remove
s1.remove(44.89)
print(s1)               # {'Kodnest', True, 400, 20, 10}

# pop without index delete random element and return one ele
popped_ele = s1.pop()
print(popped_ele)       # 400
print(s1)               # {True, 20, 'Kodnest', 10}

# delete will delete full set
# del s1                  