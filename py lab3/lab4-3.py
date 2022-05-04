def LastNlines(fname, n):
    with open(fname) as f:
        for line in (f.readlines() [-n:]):
            print(line, end ='')


fname = 'test.txt'
n=input("Enter the no of lines : ")
n=int(n)
LastNlines(fname, n)

