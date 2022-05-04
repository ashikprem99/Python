x=input("Enter the text to append to file")
f = open("test.txt", "a")
f.write(x)
f.close()
print(x," has been appended to file")


