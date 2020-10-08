print('Welcome to Weight Planet Counter!')
print('Planet Selection : Earth, Jupiter, Moon')
a=input('Please Pick The Planet You Would Like To Choose: ')
w = float(input('Please Input Your Body Weight: '))
if a=='Earth':
    def calc_weight_on_planet(w,g):
        print('Your Weight on Earth is', w)
    calc_weight_on_planet(w,9.8)
elif a=='Jupiter':
    def calc_weight_on_planet(w,g):
        w1=w/g
        w2=w1*23.1
        print('Your Weight on Jupiter is',w2)
    calc_weight_on_planet(w,9.8)
else:
    def calc_weight_on_planet(w,g):
        w1=w/g
        w2=w1*1.6
        print('Your Weight on Moon is',w2)
    calc_weight_on_planet(w,9.8)
