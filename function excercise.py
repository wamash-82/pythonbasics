#function tht adds 2 numbers
#function that calculates area of a square
#function that determines if a number is even or odd(num%2==0)
#function that deteermines maximum of two numbers
#function that calculates area of a circle(3.14*r*r)

def maxno(no1, no2):
    return max(no1, no2)
print(maxno(500,100))
def addition(x,y):
    print("Addition of",x,"and",y,"is",x+y,)
addition(20,13)
def rec(l,):
    print("Area of rec with length",l,"and width""is",l*l,)
rec(15)
def circle(r,):
    print("Area of a circle of radius",r,"is",3.142*r*r)
circle(7)
def typeno(no):
    print("Number is even" if no%2==0 else"Number is odd")
typeno(7)

#Lamda/Anonymous function
#lamda function that adds two numbers
x=lambda a,b:a+b
print(x(50,20))
#lamda function that adds three numbers
y=lambda a,b,c:a+b+c
print(y(16,34,30))
#lambda function that multiplies 2 numbers
z=lambda a,b:a*b
print(z(30,24))
