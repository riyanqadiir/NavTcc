# Q3: Employee Class with Total Employee Count
class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def total_employees(cls):
        return cls.employee_count

# Demo
e1 = Employee("John", 50000)
e2 = Employee("Sara", 60000)
print("Total Employees:", Employee.total_employees())
