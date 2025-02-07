#Elif: for adding another condition to test if the condition is false
x=5
if x>10:
    print(x,"is greater than 10")
elif x==5:
    print(x,"is equal to five")
else:
    print(x,"is not greater than or equal to five")
#Write a program that asks user for age then
#Following
#18-25=Young adult
#26-40=adult
#41 and above=mature
#below 18=child
age=int(input("What's your age?"))
if age>=18 and age<=25:
    print("Hi!,you're a young adult")
elif age>=26 and age<=40:
    print("Hi!,you're an adult")
elif age>40:
    print("Hi!,you're mature")
else :\
    print("Hi!,you're a child")
# Write a program which asks for marks and gives the grade depending on the marks given
marks=int(input("Enter your marks."))
if marks>=80 and marks<=100:
    print("Grade A")
elif marks>=70 and marks<=80:
    print("Grade B")
elif marks>=60 and marks<=70:
    print("Grade C")
elif marks>=50 and marks<=60:
    print("Grade D")
else:
    print("Fail")