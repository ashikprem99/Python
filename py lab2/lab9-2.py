my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple)
x=input("enter the element of the tuple : ")
for i in range(0,len(my_tuple),1):
    if(my_tuple[i]==x):
        print("the index of ",x,"is :",i)
