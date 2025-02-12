class Car:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
    def carinfo(self):
        return f'This is a {self.color} {self.brand}'
#Create objects
car1=Car("black","BMW")
car2=Car("grey","Cadillac")
#Accessing attributes
print(car1.brand)
#calling the method
print(car1.carinfo())
print(car2.carinfo())