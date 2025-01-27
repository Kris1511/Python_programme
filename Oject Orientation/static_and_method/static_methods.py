class MathOperations:
    @staticmethod               # Static method decorator
    def add(a, b):              # Static method definition (no self parameter)
        return a + b
    
    def calc(self):
        pass

result = MathOperations.add(10, 20)  # Calling static method
print(result)                        # Output: 30

math_op = MathOperations()           # Creating object of MathOperations class  
print(math_op.add(10, 20))           # Output: 30