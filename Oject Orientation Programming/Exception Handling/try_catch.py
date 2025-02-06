# try: Used to keep the logic in which we may get som error
# except: Will be executed when exception occurs in try block.
# else: will be executed if no exception occurs in try block.
# finally: will always executed irrespective of exception occurs or not.


def display(a, b):
    try:
        print(a / b)
    
    except:
        print("Exception Occured")

display(10, 0)        # Exception Occured
display(10, 2)        # 5.0
display(10, "2")      # Exception Occured
display(10, 5)        # 2.0