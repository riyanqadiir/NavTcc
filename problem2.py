# Q.No.2:- In a Student Management System, all students belong to the same university. How would you design a Student class with instance variables for name and age, along with a class variable university set to a default value like "ABC University"? Can you create a method that updates the university name for all students and show how changing this class variable affects all instances?

class Student:
    university = "ABC University"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def update_name(self,newname):
        self.university = newname
        print(self.university)
        
s1 = Student("Ali", 21)
s2 = Student("Zara", 23)
print(s1.university)
print(s2.university)
Student.update_name("XYZ University")
print(s1.university)
print(s2.university)

