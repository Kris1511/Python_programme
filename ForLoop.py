# for control_variables in iterable object:

# range(5) -----> go to end of 5
# range(1, 5) ------> start from 1 to 5
# range(1, 10, 2) -----> start from 1 to 10 with step 2   
# range(10, 1, -1) -----> start from 10 to 1 with step -1


# for i in 'Kodnest':
#     print(i)     # print(i, end="-") give double quotes it will print in same line

# for j in [10, 40, 30]:
#     print(j, end=" \n")


# for m in range(5):
#     print(m)

# for num in range(1, 11):
#     print(num)

# for k in range(11, 21, 2):
#     print(k, end=" ")   # print(k, end=" ") give double quotes it will print in same line
#     print()
# # wap to print all even numbers between 1 to 10

# for l in range(1, 11):
#     if l % 2 == 0:
#         print(l, end=" ")


# while loop
# i = 0
# while(i <= 10):
#     print(i)
#     i += 1


# jump statements
# wap to print numbers from 1 - 10 but if number is 6 then skip printing that number
for n in range(1, 11):
    if n == 6:
        continue
print(n)

# wap to print numbers from 1 - 10 but if number is 5 then stop printing
for d in range(1, 11):
    if d == 5:
        break
print(d)

# pass statement
def display():
    pass    # pass is used to avoid error (or) like placeholder for future code

display()

def demo():
    pass
demo()