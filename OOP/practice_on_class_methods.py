class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_avg(self):
        sum=0
        for x in self.marks:
         sum+=x
    
        print("Your average mark is", sum/3)
    
s1=Student("Hello Nahin",[91,95,90])
print(s1.name)
s1.get_avg()
    
        