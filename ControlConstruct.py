# 1. Control Construct - If Else, Elif, Nested If Else
# 2. looping statements - For, While, Nested Loops
# 3. jumping statements - Break, Continue, Pass

# 1.
def checkAge(age):
    if (age > 18):
        print("Age is greater than 18")
    else:
        print("Age is less than 18")

checkAge(34)

# 2. wap to display 'child' if age is less than 18, 'teen' if age is above than 18, 'adult' 
# if age is less than 60, 'Citizen' if age is greater than 65

def displayAge(age):
    if(age < 18):
        print('Child')
    elif(age > 18 and age < 65 ):
        print('Adult')
    elif(age > 65):
        print('Senior Citizen')
displayAge(int(input('Enter the age: ')))