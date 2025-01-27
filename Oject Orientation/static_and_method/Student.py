class Student:
    college_name = 'XYZ'

    def get_info(self):
        print(f'College Name: ', Student.college_name)

    @classmethod
    def change_name(cls, name):
        cls.college_name = name

s1 = Student()
s1.get_info()  # Output: College Name:  XYZ
Student.change_name('ABC')
s1.get_info()  # Output: College Name:  ABC