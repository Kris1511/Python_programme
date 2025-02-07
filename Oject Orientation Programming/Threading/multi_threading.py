import threading
import time
# print(threading.current_thread())

li_1 = [1, 2, 3, 4, 5]

li_2 = ['a', 'b', 'c', 'd', 'e', 'f']

def display1(li_1):
    for i in li_1:
        print(i)
        time.sleep(2)

def display2(li_2):
    for i in li_2:
        print(i)
        time.sleep(1)

t1 = threading.Thread(target = display1, args = (li_1,), name = 'Thread 1')
t2 = threading.Thread(target = display2, args = (li_2,), name = 'Thread 2')

t1.start()
t1.join()         # This will make the main thread wait for t1 to finish
t2.start()