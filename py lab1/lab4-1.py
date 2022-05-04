#LAB4
num = input ( "Enter the number to find out the divisors : " )
num = int(num)
i=1
a=[]
for i in range(i,num+1,1):
    if (num%i == 0):
        a.append(i)
print ("The divisors of the number ",num,"are : ",a)
