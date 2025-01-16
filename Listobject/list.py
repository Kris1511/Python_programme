'''
1. In list we can store homogeneous as well as heterogeneous data.
2. In list we can store duplicate data.
3. list is an ordered collection of data: order of insertion will remain as it is in the output.
4. list is mutable: we can change the data.  
'''

li1 = [10, 20, 44.45, True, 'Python', 20]
print(li1, type(li1))

# append will add element at the end of the list.

li1.append(100)         # list is mutable: we can change the data.
print(li1)              # [10, 20, 44.45, True, 'Python', 20, 100]


# insert will add element at the specified index.
# insert(index, element)
li1.insert(2, 200)
print(li1)              # [10, 20, 200, 44.45, True, 'Python', 20, 100]

li1.remove(20)          # remove will remove the first occurrence of the element.
print(li1)              # [10, 200, 44.45, True, 'Python', 20, 100]

# remove 20 all from the list. and no return element.
for i in li1:
    if i == 20:
        li1.remove(i)
    print(li1)          # [10, 200, 44.45, True, 'Python', 100]

# pop without argument will remove the element and return the last element.
remove_ele = li1.pop()
print(remove_ele)       # 100
print(li1)              # [10, 200, 44.45, True, 'Python']

# pop(index) with argument will delete the ele. at specified index.
li1.pop(4)
print(li1)              # [10, 200, 44.45, True]


# del keyword no return type
del li1[1]
print(li1)              # [10, 44.45, True]


# completed are fully deleted.
del li1
print(li1)  # error : name 'li1' is not defined