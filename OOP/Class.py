class Car:
    model="BMW"
    color="Yellow" #class attribute
    
    def __init__(self,color,cc):
     self.color=color #object attribute. Object attribute > class attribute
     self.cc=cc
     print("Adding car configurations in database")
     
    def welcome(self): #method
        print("Welcome to the era of", c1.model)
        
    def get_color(self): #method
        return self.color
    
c1=Car("Blue",1500)
c1.welcome()
print(c1.color,c1.cc)

c2=Car("Black",1800)
print(c2.cc)
print(c2.get_color())

print(Car.model)
    
    