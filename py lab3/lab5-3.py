f=open("test.txt","r")
list=[]
for line in f.readlines():
    list.append(line)
print(list)
