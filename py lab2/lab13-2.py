def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
list=[]
size=input("enter the size of the list ")
size=int(size)
for i in range(0,size,1):
    e=input("Enter an integer")
    e=int(e)
    list.append(e)
print(sub_lists(list))
