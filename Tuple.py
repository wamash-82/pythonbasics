#Tuples are ordered, immutable and allow duplicates
units=("html","css","javascript","python","django")
print(units)
print(type(units))
#Accesing items
print(units[1])
print(units[2:])
#Loop
for i in units:
    print(i)
#Tuple constructor
numbers=tuple((45,7,39,22,16))
print(numbers)
print(type(numbers))
#Loop through the items
for x in numbers:
    print(x)

