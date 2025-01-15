row = 4
col = 7

for i in range(0, row):             # here row means 4 - 1 = 3 by default
    for j in range(i, row):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    for j in range(i + 1):
        print("*", end = " ")
    print()
for i in range(1, row):             # here row means 4 - 1 = 3 by default
    for j in range(i + 1):
        print(" ", end = " ")
    for j in range(i, row):
        print("*", end = " ")
    for j in range(i, row - 1):
        print("*", end = " ")
    print()