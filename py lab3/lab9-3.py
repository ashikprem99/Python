f=open("test.txt","r")
c=0
for line in f.readlines():
    c=c+1
print("the no of lines in the file is",c)
