# Q4: Math Utility Class with Static Method
class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

# Demo
print(MathOperations.add_numbers(3, 5))
math_util = MathOperations()
print(math_util.add_numbers(10, 20))
