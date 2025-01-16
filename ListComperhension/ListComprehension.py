# syntax of list comprehension

# [expression i for in ]


li1 = [1, 2, 3, 4, 5, 6]
print(li1)                  # [1, 2, 3, 4, 5, 6]

square_li = []
# how to square
for i in li1:
    square_li.append(i ** 2)
print(square_li)            # [1, 4, 9, 16, 25, 36]

duplicate_li1 = [i for i in li1]
even = [i for i in li1 if i % 2 == 0]       #  when we have only if condition after for loop********
square_li = [i**2 for i in li1]
new_li1 = [i + 2 for i in li1]
print(duplicate_li1)
print(even)
print(square_li)
print(new_li1)              # [3, 4, 5, 6, 7, 8]

# if and else condition

li = [1, 2, 3, 4, 5]

# here when we have if and else condition  before if and after condition else******
even_odd = ['even' if i % 2 == 0 else 'odd' for i in li]
print(even_odd)             # ['odd', 'even', 'odd', 'even', 'odd']


# multiple nested for loop******
li2 = [[10, 20], [30, 40], [50, 60]]

new_li2 = [ele for sublist in li2 for ele in sublist]           # i = [10, 20]  ele = 10
print(new_li2)              # [10, 20, 30, 40, 50, 60]