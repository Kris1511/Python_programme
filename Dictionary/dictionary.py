'''
1. In dict we can't store the duplicate key.
2. In dict is we can store duplicate value.
3. In dict are mutable.
'''


d1 = {'name' : "Hari", 'age' : 30, 'phone' : 8298928323, 'age' : 45}
print(d1, type(d1))                 # {'name': 'Hari', 'age': 30, 'phone': 8298928323} <class 'dict'>
                                    # {'name': 'Hari', 'age': 45, 'phone': 8298928323} <class 'dict'> age changed

d1['name'] = 'Arun'
print(d1)                           # {'name': 'Arun', 'age': 30, 'phone': 8298928323}

marks = { 'sci' : 78, 'math' : 90}      # In dict is we can store duplicate value.


# get keys only 
for i in d1.keys():                 # name
    print(i)                        # age
                                    # phone
    
# get values only                   
# Arun
# 45
# 8298928323
for j in d1.values():
    print(j)

# get items means key, value pair
# ('name', 'Arun')
# ('age', 45)
# ('phone', 8298928323)
for k in d1.items():
    print(k)