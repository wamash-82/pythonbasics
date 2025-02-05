#Lists are ordered, mutable/changeable and allow duplicates
students=["Ruth","Grace","Mark","Muchai"]
print(students)
#Accesing the items
print(students[0])
print(students[2])
print(students[-1])
#Len()
print(len(students))

#Adding items
#Append() add to the end
students.append("Dorean")
print(students)
#Insert()n add item at a given index
students.insert(0, "Makena")
print(students)
#Change item
students[2]="Aleko"
print(students)
#Remove list item
students.remove("Mark")
print(students)
#Pop() removes the last item
students.pop()
print(students)
#Sort; arranges items alphabetically
students.sort()
print(students)
#Copy
newstuds=students.copy()

#List Constructer
fruits=list(("oranges","bananas","cherry","strawberry"))
print(fruits)
print(type(fruits))
#Join list extend() adds a second list at the end of first list
newstuds.extend(fruits)
print(newstuds)
#Clear
newstuds.clear()
print(newstuds)
#Loop through the items
for x in students:
    print(x)
