string=input("Enter the string to calculate the frequency :")
string=string.lower()
split=string.split(" ")
print(split)
fre={}
for i in split:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print("The frequnecy count of the given string is : ", str(fre))

