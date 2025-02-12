with open("examle.txt","w")as y:
    y.write("Hyyy everyone \n")
    y.write("This is python \n")
#append
with open("example.txt","a")as y:
    y.write("New line appended \n")
#read
with open("example.txt","r")as x:
    print(x.read())
