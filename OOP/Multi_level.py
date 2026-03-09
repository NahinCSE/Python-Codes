class Car:
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
    
class Honda(Car):
    def __init__(self, name):
        self.name = name

class Model(Honda):
    def __init__(self,model):
        self.model=model
        
c1=Model("Racer")
c1.stop()