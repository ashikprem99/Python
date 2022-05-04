n=input("Enter the value for n : ")
print("The seires is : n+(n-2)+(n-4)... (until n-x =< 0)")
n=int(n)
sum = 0
while (n>=0):
  sum = sum + n;
  n = n - 2;
print("sum of the series is :", sum)
