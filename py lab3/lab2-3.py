n=input("enter the no of lines to read : ")
n=int(n)
f = open("test.txt", "r")
for i in range(0,n,1):
    print(f.readline())
