# Inheritance method used to inherit the properties of the parent class to the child class.
# Inheritance method is used to reduce the code redundancy.


class Student:
    def cook(self):
        print('Student is cooking biryani')

    def play(self):
        print('Student is playing cricket')

class Employee(Student):

    # specialized method
    def work(self):
        print('Employee is working in MNC')

    # overriding method
    def cook(self):
        print('Employee is cooking pulav')

emp = Employee()
emp.play()                  # Student is playing cricket
emp.cook()                  # Employee is cooking pulav
emp.work()                  # Employee is working in MNC