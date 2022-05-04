my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple)
rev=[]
j=-1

for i in my_tuple:
    rev.append(my_tuple[j])
    j=j-1
print("the reverse of the tuple is :",''.join(rev))
    
