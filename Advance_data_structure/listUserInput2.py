# li = input('Enter the elements: ')
# print(li, type(li))         # 34 493 2382 <class 'str'>

# li2 = li.split()
# print(li2)                  # ['34', '493', '2382']

# li3 = list(map(int, li2))
# print(li3)                  # [45, 32, 53]


# above line of code we can use one line of code, *give space click*
tup = tuple(map(int, input('Enter the element: ').split()))
print(tup)                  # (45, 282, 489, 2348)

ans = list(map(int, input('enter the element: ').split()))
print(i for i in ans if i % 2 == 0)