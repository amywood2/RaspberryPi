import datetime

name = input("Pleas enter your name: ")


dt = datetime.datetime.now()
hours = dt.hour
minutes = dt.minute
if hours >= 0 and hours<=11 :
    message = "Good morning %s, the time is : %d:%d"%(name, hours, minutes)
    print(message)

elif hours >= 12 and hours <=17 :
    message = "Good afternoon %s, the time is : %d:%d"%(name, hours, minutes)
    print(message)
else :
    message = "Good evening %s, the time is : %d:%d"%(name, hours, minutes)
    print(message)
