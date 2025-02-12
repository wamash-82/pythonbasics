class Employee:
    def __init__(self,name,age,salary,job_title):
        self.name=name
        self.age=age
        self.salary=salary
        self.job_title=job_title
    def displayinfo(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Salary: { self.salary}')
    def inc_sal(self,amount):
        self.salary+=amount
        print(f'The salary of {self.name} has increased to {self.salary}')
    def get_annual_sal(self):
        return self.salary *12
    def change_name(self,new_name):
        self.name=new_name
        print(f'Employees name updated to {self.name}')
    def change_dep(self,new_job_title):
        self.job_title=new_job_title
        print(f'{self.name} was changed to {self.job_title}')
#create an object
emp1=Employee("Justin",21,50000,"accountant")
emp2=Employee("Vee",23,30000,"HR Manager")
print(emp1.name)
print(emp2.age)
emp1.displayinfo() #calling
emp2.displayinfo()
emp2.inc_sal(15000)
emp1.inc_sal(25000)
print(f'The annual salary of {emp1.name},who is an {emp1.job_title},is {emp1.get_annual_sal()}')
print(f'The annual salary of {emp2.name},who is a {emp2.job_title},is {emp1.get_annual_sal()}')
#change name
emp1.change_name("Wamaitha")
emp1.change_dep("Deputy Director")
emp2.change_dep("CEO")
#inherit from employee class
class Manager(Employee):
    def __init__(self,name,age,salary,job_title,team_size):
        super().__init__(name,age,salary,job_title)
        self.team_size=team_size
    def displayinfo(self):
        super().displayinfo()
        print(f'Team size: {self.team_size}')
#create an object
mgr=Manager("Jack",20,90000,"Manager",15)
mgr.displayinfo()