# NameMangling is the process of providing new name to the private variable.
# These new names will be provided automatically by the python for all private members.
# New name will be provided in format :
# objectName._className__variableName

class Demo1:
    def __init__(self, name):
        self.__name = name

d1 = Demo1("Raj")
print(d1._Demo1__name)          # Raj -> print(objectName._className__variableName)