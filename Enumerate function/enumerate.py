# enumerate function
li = [10, 20, 30, 40, 50]

for i, ele in enumerate(li):            # enumerate function
    print(f"I is {i} and element is {ele}")

# write a python to print odd and even index number
for i, ele in enumerate(li):
    if i % 2 == 0:
                                        # index is:  0 10
                                        # index is:  2 30
                                        # index is:  4 50
        print("index is: ", i, ele)

