
#if:executes a block of code if the given condition is true
#If condition:
        #Block of code to be executed
        #If the condition is true
x=3
if x<5:
    print(x,"is less than five")
#Else: specifies the code to be executed
#if the condition is false
i=8
if i>10:
    print(i,"is greater than 10")
else:
    print(i,"is less than 10")
#A progaram that asks user for age.If age is greater than or
#Equal to 18,user can drive else they cannot
age=int(input("what is your age?"))
if age>=18:
    print("You can drive")
else:
    print("You cannot drive")
#Write a program that gets a number from user then checks if It's odd or even
num=int(input("Enter any number"))
if num/2 and num%2==0:
    print("is an even number")
else:
    print("is an odd number")
#Write a program that gets two numbers from user then checks