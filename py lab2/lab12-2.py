list=[]
size=input("enter the size of the list ")
size=int(size)
for i in range(0,size,1):
    e=input("Enter a character")
    list.append(e)
print(list)
x=''.join(list)
print("the string is ",x)
