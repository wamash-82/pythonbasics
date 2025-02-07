#Dictionaries are used to store data in key value pairs
#Items are ordered, changeable, and do not allow duplicates
student={
    "Name":"Wamaitha",
    "Age":18,
    "City":"Nairobi"}
print(student)
#Accessing the value
print(student["Name"])
print(student["City"])
#Print all keys.keys()
print(student.keys())
#Print all values
print(student.values())
print(type(student))
#Print a list of key:value pairs
print(student.items())
#Change items
student["Name"]="Ruth"
print(student)
#Add item
student["course"]="Fullstack"
print(student)
#Print all the keys one by one loop
#print all the values one by one
#print all key:value pair one by one
for x,y in student.items():
    print(x,y)
for x in student.keys():
    print(x)
for y in student.values():
    print(y)