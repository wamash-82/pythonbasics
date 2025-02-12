#Class is a blueprint for creating something
#Object is an instance of a class
#student class:fname,sname,course,age
class Student:
    def __init__(self,fname,sname,course,age):
        self.fname=fname
        self.sname=sname
        self.course=course
        self.age=age
    def __str__(self):
        return f'{self.fname} {self.sname} {self.course} {self.age}'
    def get_full_name(self):
        return f'{self.fname} {self.sname}'
    def intro(self):
        print(f'Hello my name is {self.fname} amd I am learning {self.course}')
    def _get_email(self):
        return f'{self.fname}{self.sname}@emobilis.ac.ke'
#Creating an object
stud1=Student("Jane","Njoroge","Cyber security","25")
stud2=Student("Mwiathi","Brian","Web Development","21")
print(stud1)
print(stud2)
#accessing attributes
print(stud1.fname)
#Calling a method
print(stud1.get_full_name())
print(stud2.get_full_name())
stud1.intro()
print(stud1._get_email())
print(stud2._get_email())