# find runner-up score

# li = list(map(int, input().split()))

# li1 = set(list(li))

# li.sort(reverse = 'True')
# print(li)
# print(li[1])            # [5, 4, 4, 3, 2]
#  output: 4


# second smallest number

# li2 = list(map(int, input().split()))

# lii = set(list(li2))        # {}  - remove duplicate value

# li3 = list(lii)             # []  - again add the list

# li2.sort()                  # sort method won't return anything (none) will return
# print(li2)          # [1, 2, 4, 4, 5, 6]
# print(li3[-2])          #  5  - second largest number
# print(li3[-1])          #  6 -  largest number

# print(li3[0])           # 1 -  smallest element
# print(li3[1])           # 2 -  second smallest element


# un-packing

name, *marks, age = ["Rahul", 100, 75, 85, 35]
print(name)         # Rahul
print(marks)        # [100, 75, 85]
print(age)          # 35


