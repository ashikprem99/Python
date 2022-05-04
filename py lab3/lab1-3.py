x=input("ENTER THE TEXT TO WRITE :")
f = open("test.txt", "a")
x=x+"\n"
f.write(x)
f.close()
f = open("test.txt", "r")
print(f.read())
f.close()
