#LAB2 ODD OR EVEN

name=input("Enter your Name : ")
def oddeven(x):
    x=int(x)
    if(x%2==0):
        print("Hey",name,"the value entered is a even number")

    elif(x%2!=0):
        print("Hey",name,"the value entered is a odd number")
    print("enter again to exit ")
while 1:
    value=input("Enter a Digit : ")
    if(value==""):
        break
    else:
        value=oddeven(value)

    
