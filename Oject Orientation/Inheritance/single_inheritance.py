class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee_info(self):
        self.display_person_info()
        print(f'Employee ID: {self.employee_id}')


name = input("Enter the name: ")
age = int(input("Enter the age: "))
employee_id = input("Enter the employee ID: ")

emp = Employee(name, age, employee_id)
emp.display_employee_info()