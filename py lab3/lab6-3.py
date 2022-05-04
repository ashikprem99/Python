f=open("test.txt","r")
var=''
for line in f.readlines():
    var = var+line
print(var)
