item=input("Enter the item to remove from the set : ")
item=int(item)
my_set = {1, 2, 3,4,6,7,8,9,0,5}
for x in my_set:
    if (item==x):
        print("item found in list and removed")
        my_set.remove(item)
        break
print(my_set)
