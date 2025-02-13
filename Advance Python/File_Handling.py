# read mood

# file = open('test.txt', 'r')
# print(file.read())

with open('test.txt', 'r') as file:
    print(file.read)

# data = file.read()
# print(data[0])
# print(file.readlines())
# print(file.readlines())


# write mood

# file1 = open('test2.txt', 'w')
# file1.write('Hello from python\n')
# file1.write('Hello fromm java')

# append mood

file1 = open('test2.txt', 'a')
file1.write('\nHello from java')
file1.close()