class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.speed=0
    def accelerate(self,amount):
        self.speed+=amount
        print(f"Car accelerated. Current speed: {self.speed}")
    def brake(self,amount):
        self.speed-=amount
        if self.speed<0:
            self.speed=0    
        print(f"Car slowed down. Current speed: {self.speed}")
car1 = Car("Maruthi", "Fortuner")
car1.accelerate(30)
car1.accelerate(20)
car1.brake(15)
car1.brake(50)