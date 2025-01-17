li = []
num = int(input("Enter the number: "))

for i in range(num):
    ele = int(input(f'Enter element at index {i}: '))
    li.append(ele)
print(li)

# output : 
# Enter the number: 4
# Enter element at index 0: 3
# Enter element at index 1: 4
# Enter element at index 2: 5
# Enter element at index 3: 2
# [3, 4, 5, 2]