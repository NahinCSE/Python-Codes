class Car:
    def __init__(self):
        self.clutch=False
        self.acc=False
        self.brake=False
    
    def start(self):
        self.clutch=True
        self.acc=True
        self.brake=True
        print("Car started")
        
c1= Car()
c1.start()