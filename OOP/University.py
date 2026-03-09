class Person:
    def __init__(self, name,email,id):
        self.name=name
        self.email=email
        self.id=id
        
    def login(self):
        pass
p1=Person(name=input("Enter your name: "),email=input("Enter your email address: "),id=input("Enter yout id no: "))
print("Here is your information:", "1)name:", p1.name,"2)mail: ", p1.email,"3)ID: ",p1.id)

class Faculty(Person):
    def __init__(self,grades,courses_teaching):
        
        self.grades=grades
        self.courses_teaching=courses_teaching
        
    def login(self):
        password=input("Enter your password: ")

        # Faculty class methods and constructor end here

# Faculty usage code (move outside the class definition)
courses_teaching_num = int(input("Enter your number of courses teaching:"))
course_grades = []
for j in range(courses_teaching_num):
    course_grade = input(f"Enter your course grades {j+1}:")
    course_grades.append(course_grade)

f1 = Faculty(grades=course_grades, courses_teaching=course_grades)
print("Grades for the courses:", f1.grades)
f1.login()

class Student(Faculty):
    def __init__(self,courses,grades,cgpa):
        self.courses=courses
        self.grades=grades
        self.cgpa=cgpa
        

    def login(self):
        password=input("Enter your password: ")
        
    def scholarship_status(self):
        if self.cgpa>=3.75:
            print("Congratulations!!You are eligible for the scholarship.")
        else:
            print("You are not eligible for the scholarship.")
            
    def probation_status(self):
        if(self.cgpa<2.5):
            print("You are on probation.")
        else:
            print("You are not on probation.")
            
    def calculate_cgpa(self):
        
        points_map = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0}
        total = 0
        for g in f1.grades:
            total += points_map.get(g.upper(), 0)
        return round(total / len(f1.grades), 2) if f1.grades else 0

    @staticmethod
    def improvement():
        print("You need improvement")

course_catalog=[]
course_num=int(input("Enter your number of courses:"))

for i in range(course_num):
    course=input(f"Enter your course name {i+1}:")
    course_catalog.append(course)

s1=Student(courses=course_catalog,grades=[],cgpa=0)
s1.login()
print("Here is your course catalog:", s1.courses)
print("Your cgpa:", s1.cgpa )
s1.calculate_cgpa()
s1.scholarship_status()
s1.probation_status()

