#hadling file not found error
try:
    with open("abc.txt","r")as x:
        print(x.read())
except FileNotFoundError:
    print("error:file not found")
#Handling ZeroDivisionError
try:
    result=3/0
    print(result)
except ZeroDivisionError:
    print("error you cannot divide a number by zero")