def display(a, b):
    try:
        print(a / b)
    
    except ZeroDivisionError:
        print("Zero Division Error")

    except NameError:
        print('Name Error')

    except TypeError:
        print('Type Error')

    except:
        print("Exception Occured")          # default always at the end

display(10, 0)        # Zero Division Error
display(10, 2)        # 5.0
display(10, "2")      # Type Error