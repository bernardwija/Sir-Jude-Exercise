print('Welcome to data configurator!')
a, b, c, d=input('Please input 4 data seperated by space to configure(1 2 3 4): ').split(',')
x = [a, b, c, d]
y = (a, b, c, d)
print(x)
print(y)
ctr=0
while True:
    z=input('Do you want to input another data to the list?(Yes or No): ')
    if z=='Yes':
        n=input('Please Input a data: ')
        x.append(n)
        print(x)
        print(y)
    else:
        print('Thankyou for using our service!')
        break
