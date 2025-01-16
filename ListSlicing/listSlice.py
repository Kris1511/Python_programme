
'''
1. list slicing is create sublist  from main list.
syntax: list_name [start : end - 1 : steps]

reverse = li1[:: -1]
last_ele = li1[-1 ::]
'''

li1 = [10, 20, 30, 40, 50, 60]
sli1 = li1[0 : 4 : 1]
print(sli1)             # [10, 20, 30, 40]

sli2 = li1[::]
print(sli2)             # [10, 20, 30, 40, 50, 60]

sli3 = li1[1::]
print(sli3)             # [20, 30, 40, 50, 60]

sli4 = li1[::2]
print(sli4)             # [10, 30, 50]

reverse_sli = li1[:: -1]
print(reverse_sli)      # [60, 50, 40, 30, 20, 10]

reverse_sli2 = li1[-1 ::]
print(reverse_sli2)     # [60]