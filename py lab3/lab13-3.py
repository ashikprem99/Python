with open('test.txt','r') as f1, open('second.txt','a') as f2:
      
    # read content from first file
    for line in f1:
             # append content to second file
             f2.write(line)

f1.close()
f2.close()
f2 = open("second.txt" ,"r")
print(f2.read())
