import math
import random
char_list = ['a','e','i','o','u']
length=len(char_list)
c=[]
for i in range(0,math.factorial(length)+1,1):
    random.shuffle(char_list)
    x=''.join(char_list)
    if(x not in c):
        c.append(x)
print("the combinations of string made from the list is :\n",c)        
    
    
