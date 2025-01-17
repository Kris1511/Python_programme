

# reverse() method reverse the original object
li = [10, 20, 30, 40, 50]
print(li)       # [10, 20, 30, 40, 50]
li.reverse()
print(li)       # [50, 40, 30, 20, 10]

# reversed(iterable_object)
li2 = [48, 32, 11, 22, 33]
li2_rev = list(reversed(li2))       # we give to the "list" then print it reverse
print(li2)        # [48, 32, 11, 22, 33]
print(li2_rev)    # [33, 22, 11, 32, 48] 

li3 = [3, 59, 20, 1, 8]
li3_rev = list(reversed(li3))       # creating new reverse list
li3.reverse()                       # reversing original list
