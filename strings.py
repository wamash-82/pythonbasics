from types import new_class

message="Hiiiiiiiii"
course='Python'
sentence="""this is an example of a multiple string"""
print(message)
print(course)
print(sentence)
#string methods abc()
#upper(),lower(), title()
greetings=("Good Afternoon")
print(greetings)
print(greetings.upper())
print(greetings.lower())
print(greetings.title())
stem=("web development")
print(stem.title())
print(stem.upper())
#replace
my_fav="I love html"
print(my_fav.replace("html", "python"))
#FIND()
var="this is python"
print(var.find("python"))
print(var.find("is"))
#string slicing
mycourse="fullstack"
print(mycourse[0:4]) # 0 to 3
print(mycourse[:2]) #0 to 1
print(mycourse[4:]) #4 to end
print(mycourse[-3:]) #last 3 characters
#indexing
text="python"
print(text[0])
print(text[2])
print(text[-1])
#escape characters \
print("this is a message \n in a new line")
print("name \t course")
print("She said \"hello\"")
print("He said \"It's Momday morning\"")
print('"Any body can learn" by Barack Obama')
#f strings
rika="26"
name="my name is john" + rika
print(name)
