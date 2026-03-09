#this is an example of single inharitance class
#Single Inheritance
class Car:
    color="Mica Blue"
    def start(self):
        print("Car has been started")
    @staticmethod
    def stop():
        print("Car has been stopped")
        
class Toyota(Car):
    def __init__(self,name,model):
      self.name=name
      self.model=model
      
c1=Toyota("Premio","G-Superior")
c2=Toyota("Crown","Deluxe")

print(c1.name,c1.model)  # This will print "Premio G-Superior"
print(c2.name,c2.model)  # This will print "Crown Deluxe"

print(c1.stop()) # This wil print the car has been stopped
print(c2.start())  # This will print "Car has been started"
print("The color of Premio G-Superior is",c1.color)  # This will print "Mica Blue"