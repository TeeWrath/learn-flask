class Student:
    def __init__(self):
        self.name = "subroto"
        

student = Student()
print(student.name)

class ClassTest:
    @classmethod
    def methodClass(cls):
        print(f"instance of {cls}")

ClassTest.methodClass()