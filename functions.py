#Function
def func():
    print("Tadaa! This is a function.")
#Calling the function
func()
#Another function
def greetings():
    print("Hyy! How are you?")
#calling
greetings()

def classes():
    print("My classes are just basically about coding.")
classes()
#Function with parameter
def habari(fname):
    print("Umeshindaje?",fname)
habari("Fifi")
habari("Luke")
#function wuth two parameters
#a function that calculates the area of a rectangle
def Aofrec(l,w):
    print("Area of rec with length",l,"and width",w,"is",l*w,)
#calling
Aofrec(50,20)
Aofrec(16,25)
#function with a default parameter
def func2(name="Agatha",age=22):
    print("Hello",name,"you are",age,"years old")
func2("Mary",13)
func2()
#return
def example(x):
    return x*5
answer=example(5)
print(answer)
print(example(2))
