color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
f = open("test.txt","a")
for c in color:
    f.write("%s\n" %c)
f.close()
f = open("test.txt","r")
print(f.read())

