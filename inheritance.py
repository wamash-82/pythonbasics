#parent/super class
from employee import Employee


class animal:
    def __init__(self,name):
        self.name=name
    def supermethod(self):
        print("Hello from super class")
    def speak(self):
        print("Hello hello")
#a child class that inherits from animal class
class Dog(animal):
    def submethod(self):
        print('Hello from sub method')
    def speak(self):
        print(f'{self.name} does whoo! whoo!')
#Create an object
mydog=Dog("Snowy")
print(mydog.name)
#calling a method within the parent class
mydog.submethod()
class cat(animal):
    pass
mycat=cat("Parsley")
print(mycat.name)
mycat.supermethod()
mycat.speak()
mydog.speak()

