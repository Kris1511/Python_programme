li = [30, 28, 10, 59, 40]
li.sort()
print(li)           # [10, 28, 30, 40, 59]   => ascending

li.sort(reverse=True)
print(li)           # [59, 40, 30, 28, 10]   => 

li2 = [100, 20, 39, 78, 45]
print(li2)          # [100, 20, 39, 78, 45]
sorted_li2 = sorted(li2)
print(sorted_li2)   # [20, 39, 45, 78, 100]