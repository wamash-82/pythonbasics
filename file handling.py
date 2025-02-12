#open(filename,mode)
#r-read,w-write,a-append
x=open("demo.txt","w")
x.write("I'm learning python \n")
x.close()
#append
x=open("demo.txt","a")
x.write("This is a new line appended \n")
x.close()
#read
x=open("demo.txt","r")
print(x.read())
x.close()