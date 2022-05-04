#LAB 8
import random
gen = [0,1,2,3,4,5,6,7,8,9]
print("GUESS THE NUMBER")
ran = random.choices(gen,k=1)
print(ran)
flag = 1
val = input("enter your guess : ")
val=int(val)
while (flag!=0):
    if (val==ran[0]):
        print("WONDERFUL GUESS!")
        i=0
        break
    elif (val >> ran[0]):
        print("too high!")
        
        val = input("enter your guess : ")
        val=int(val)
    elif (val > ran[0]):
        print(" high!")
        val = input("enter your guess : ")
        val=int(val)
    elif (val < ran[0]):
        print("low!")
        val = input("enter your guess : ")
        val=int(val)
    elif (val << ran[0]):
        print(" too low!")
        val = input("enter your guess : ")
        val=int(val)
    else:
        if(flag==0):
            break

