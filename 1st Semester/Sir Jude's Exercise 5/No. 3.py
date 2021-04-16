import calendar
print('Welcome to Calendar Calculator!')
y = int(input("Please input the year: "))
m = int(input("Please input the month: "))
print(calendar.month(y, m, w=0, l=0))
print('Thankyou for using our service!')