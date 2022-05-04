f=open("test.txt","r")
array=[]
for line in f.readlines():
    array.append(line)
print(array)
