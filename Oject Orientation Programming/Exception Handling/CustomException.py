class PinError(Exception):
    # def __init__(self, message):
    #     self.message = message

    # def __str__(self):
    #     return self.message
    pass
    
correctPin = 1234

pin = int(input("Enter Pin: "))

try:
    if pin == correctPin:
        print("Correct Pin")
    else: 
        raise PinError("Incorrect Pin", pin)

except PinError as e:
    print("Error Message: ", e)
