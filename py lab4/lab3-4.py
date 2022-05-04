import datetime
x=input("enter the unix time stamp")
x=int(x)
print(datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))

