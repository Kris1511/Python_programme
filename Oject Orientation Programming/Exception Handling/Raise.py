def dis(a, b):
    print(a / b)
dis(10, 2)          # 5.0

# dis(10, 0)        # ZeroDivisionError: division by zero

# dis(10, 'kod')    # TypeError: unsupported operand type(s) for /: 'int' and 'str'

def checkAge(age):
    if age < 18:
        raise ValueError("Age is less than 18")
    
try:
    checkAge(12)
except ValueError as e:
    print('Error Message: ', e)