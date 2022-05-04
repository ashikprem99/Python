n=input("Enter the string : ")
split=n.split(" ")
print(split)
big=split[0]

for i in range(0,len(split),1):
    temp= split[i]
    if (len(temp)>len(big)):
        big = temp
        
print("the biggest word in the sentance is :",big)
