print('Welcome to Photo Resizer!')
print(' ')
def calc_new_height():
    w=float(input('Please Insert Your Current Photo Width: '))
    y=float(input('Please Insert Your Current Photo Height: '))
    h=w/y
    w1 = float(input('Please Insert Your New Photo Width: '))
    h1 = w1/h
    return h1
print('Here is The Corresponding Height:',calc_new_height())


