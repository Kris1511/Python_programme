class Bank:
    bank_name = "SBI"                   # class variable

    def __init__(self, name, age, balance):
        self.name = name                # instance variable
        self.age = age
        self.balance = balance

    def get_info(self):
        print(f'''User Name: {self.name} and User Balance: {self.balance} for Bank: {self.bank_name}''')

b1 = Bank('John', 25, 1000)

print(b1.bank_name)             # output: SBI
print(Bank.bank_name)           # output: SBI
b1.get_info()                   # output: User Name: John and User Balance: 1000 for Bank: SBI