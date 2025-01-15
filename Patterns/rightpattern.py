row = 5
col = 5

for i in range(0, row):             # here row means 4 - 1 = 3 by default
    for j in range(i + 1):
        print("*", end = " ")
    print()
print()

for j in range(row):
    for k in range(j, row):
        print("*", end = " ")
    print()
print()

# right passcale triangle
for i in range(0, row):             # here row means 4 - 1 = 3 by default
    for j in range(i + 1):
        print("*", end = " ")
    print()
for j in range(row):
    for k in range(j, row - 1):
        print("*", end = " ")
    print()

print()

#Butterfly pattern
for i in range(0, row):
    for j in range(i + 1):
        print("*", end = " ")
    for k in range(i, row - 1):
        print(" ", end = " ")
    for l in range(i, row - 1):
        print(" ", end =" ")
    for m in range(i + 1):
        print("*", end = " ")
    print()
for i in range(i, row):
    for j in range(i, row - 1):
        print("*", end = " ")
    for j in range(i + 1):
        print(" ", end = " ")       
    for j in range(i + 1):  
        print(" ", end = " ")   
    for j in range(i, row - 1):
        print("*", end = " ")
    print()