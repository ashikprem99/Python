list=[]
size=input("enter the size of the list ")
size=int(size)
for i in range(0,size,1):
    e=input("Enter an integer")
    e=int(e)
    list.append(e)
sum=0
for i in list:
    
    sum=sum+i
print("The sum of integers in list : ",sum)

