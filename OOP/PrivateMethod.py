class Student:
    def __init__(self,phy,che,math):
        self.phy=phy
        self.che=che
        self.math=math
        self.percentage=str((self.phy+self.che+self.math)/3)+"%"
    
    def calcpercentage(self):
        self.percentage=str((self.phy+self.che+self.math)/3)+"%"
        
s1=Student(94,96,90)
print(s1.percentage)  # This will print the percentage of marks

 #If the marks is changed...
s1.math=99
#print(s1.math)
#print(s1.percentage)#the percentage is not changing with the changed marks
s1.calcpercentage()
print(s1.percentage)  # Now the percentage is updated with the new marks


