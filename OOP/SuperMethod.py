class Car:
    def __init__(self, type):
        self.type = type
        
    def start(self):
        print("Car started")
    
    @staticmethod    
    def stop():
        print("Car stopped")
        
class Model(Car):
    def __init__(self,brand,type):
        super().start()
        super().stop() 
        self.brand=brand
        super().__init__(type)
         
        
c1 = Model("Sedan","Octane")
print(c1.brand)
print(c1.type)
        