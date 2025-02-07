#for loop-for interacting through lists, tuples, string
#Loop in string
from Lists import fruits

for x in "Hello":
    print(x)
#Loop in a list
users=["Alice","Kamau","Jonte","Fifi"]
for y in users:
    print(y)
#loop through a range
for z in range(5):
    print(z)
#break
fruits=["apple","banana","cherry","mango"]
for a in fruits:
    if a=="cherry":
        break
    print(a)
#continue
fruits=["apple","banana","cherry","mango"]
for a in fruits:
    if a=="cherry":
        continue
    print(a)