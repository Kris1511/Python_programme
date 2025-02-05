def display(a, b):
    try:
        print(a / b)
    
    except:
        print("Exception Occured")

display(10, 0)        # Exception Occured
display(10, 2)        # 5.0
display(10, "2")      # Exception Occured
display(10, 5)        # 2.0