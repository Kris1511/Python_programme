from functools import reduce

# map method
li = [1, 2, 3, 4, 5]

newLi = list(filter(lambda num : num % 2 == 0, li))
print(newLi)                    # [2, 4]


# reduce method
sum = reduce(lambda a, b : a + b, li)
print(sum)                      # 15

# map method

square = list(map(lambda num : num ** 2, li))
print(square)                   # [1, 4, 9, 16, 25]