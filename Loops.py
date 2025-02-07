#While loops-executes statements as long as condition is true
x=1
while x<5:
    print("Hello World!")
    x+=1 # increment
y=1
#print 1-10
while y<=10:
    print(y)
    y+=1
#print 0-5
r=0
while r<=5:
    print(r)
    r += 1
#break
r=0
while r<=5:
    print(r)
    if r==3:
        break
    r+=1
#continue
n=0
while n<=5:
    n+= 1
    if n==3:
        continue
    print(n)

