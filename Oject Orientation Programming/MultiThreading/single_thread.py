import time

li_1 = [1, 2, 3, 4, 5]

li_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def display1(li_1):
    for i in li_1:
        print(i)
        time.sleep(1)

def display2(li_2):
    for i in li_2:
        print(i)
        time.sleep(1)

display1(li_1)
display2(li_2)