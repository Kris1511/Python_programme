class Employee:
    company_name = 'code'
    def __init__(self, name, age, design):
        self.name = name
        self.age = age
        self.design = design

    def login(self, time):
        print(f'{self.name} is logged in at {time}')

    def logout(self, time):
        print(f'{self.name} is logged out at {time}')

    def work(self, time):
        print(f'{self.name} is working for {time} hours')

    def devDetails(self):
        print(f'{self.name} is a {self.design} and is {self.age} years old')

e1 = Employee('John', 25, 'SDE')
e2 = Employee('Doe', 30, 'Manager')
e3 = Employee('Jane', 35, 'SDE-III')

e1.devDetails()
e2.devDetails()
e3.devDetails()


# output:

# John is a SDE and is 25 years old

# Doe is a Manager and is 30 years old

# Jane is a SDE-III and is 35 years old
