from datetime import datetime

#LAB QUESTION 1

print("Find when u become 100 yrs old")
print("-------------------------------")
name  =  input(" please enter your name :")  #user input name
age   =  input("please enter your age :")    #user input age
print("hello", name ,"nice to meet you !")

def age100calculator(x):                     #function for calculating the year in whoch user turns 100
    x=int(x)
    year_now = datetime.now()                #calculates the current date
    print(year_now)
    year = year_now.strftime("%Y")           #from the current date calculates the year 
    year=int(year)
    age100 =(year-x)+100                     #finds the year in which user turns 100
    return age100                            #returns that year

age100 = age100calculator(age)

print("you become 100 in year :",age100)

    

