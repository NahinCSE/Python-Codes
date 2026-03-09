class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    @staticmethod #decoretor
    def Hello():
        print("Hello")

    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(self.name, " your average marks is: ",sum/3)
    
s1 = Student("Junaid", [90, 89, 92])
s1.Hello()
s1.avg()

s2 = Student("Ehsan",[91,99,96])
s2.avg()