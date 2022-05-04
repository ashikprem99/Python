string=input("Enter the string to calculate the length :")
count=0

for i in range(0,len(string),1):
    count=1
    for j in range(i+1,len(string),1):
        if (string[i]==string[j] and string[i] != ''):
            count=count+1
        
    if(count>1 and string[i] !=''):
        print(string[i],count)
            
            
    

