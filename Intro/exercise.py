#Exercie 1
#Import dates from datetime module and print today's date
from datetime import date
print(date.today())
#Print the current date
print("Today's date is: " + str(date.today()))
#Print the current year    
print("This year is: " + str(date.today().year))
month = date.today().month
#Print the current month
if month == 1:
    print("This month is: January")
elif month == 2:
    print("This month is: February")
elif month == 3:
    print("This month is: March")
elif month == 4:
    print("This month is: April")
elif month == 5:
    print("This month is: May")
elif month == 6:
    print("This month is: June")
elif month == 7:
    print("This month is: July")
elif month == 8:
    print("This month is: August")
elif month == 9:
    print("This month is: September")
elif month == 10:
    print("This month is: October")
elif month == 11:
    print("This month is: November")
elif month == 12:
    print("This month is: December")
else:
    print("This month is: " + str(date.today().month))
#Print the current day
if date.today().day == 1 or 21 or 31:
    print("Today is: " + str(date.today().day) + "st")
elif date.today().day == 2 or 22:
    print("Today is: " + str(date.today().day) + "nd")
elif date.today().day == 3 or 23:
    print("Today is: " + str(date.today().day) + "rd")
else:
    print("Today is: " + str(date.today().day) + "th") 

