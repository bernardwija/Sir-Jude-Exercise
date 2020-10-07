print('Welcome to Weight Planet Counter!')
print('Planet Selection : Earth, Jupiter')
a=input('Please Pick The Planet You Would Like To Choose: ')
w=float(input('Please Input Your Body Weight: '))
if a=='Earth':
    print('Your Weight on Earth is', w)
else:
    def calc_weight_on_planet():
        f=w/9.8*23.1
        return f
    def main():
        print(' ')
        print('Your Weight on Jupiter is',calc_weight_on_planet())
    main()

