# Input method will always text and input as a string.
# division result will be in float.

# ex 1:
num1 = input("Enter a number: ")
print('Value of num1 is: ' , num1 , ' Data type of num1 is: ' , type(num1))

# ex 2
num2 = int(input("Enter a number: "))       # convert into integer
print('Value of num1 is: ' , num2 , ' Data type of num1 is: ' , type(num2))

print(f'Addition of {num1} and {num2} is: {int(num1) + num2}')   # convert into integer
print(f'Subtraction of {num1} and {num2} is: {int(num1) - num2}')   # convert into integer
print(f'Multiplication of {num1} and {num2} is: {int(num1) * num2}')   # convert into integer
print(f'Division of {num1} and {num2} is: {int(num1) / num2}')   # output always in float