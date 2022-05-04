#LAB 6

string = input( " Enter a string to check if palindrome or not :" )
i=len(string)

j=-1
rev=[]
for i in range(0,i,1):
    rev.append(string[j])
    j=j-1

if list(string) == list(rev):
   print("The string ",string," is a palindrome.")
else:
   print("The string ",string," is not a palindrome.")

