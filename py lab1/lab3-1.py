#LAB 3
print("The given list is A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] ")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num1 = input("Enter the limit value of the list : ") 
num1 = int(num1)
i=0
print ( "the elements in the list under the range ",num1," are :" )
for i in range(i,len(a),1):
    if(a[i]<5):
        print (a[i])
        i=i+1
    else:
        i=i+1

    
