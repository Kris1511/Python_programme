# find runner-up score

li = list(map(int, input().split()))

li1 = set(list(li))

li.sort(reverse = 'True')
print(li)
print(li[1])            # [5, 4, 4, 3, 2]
#  output: 4