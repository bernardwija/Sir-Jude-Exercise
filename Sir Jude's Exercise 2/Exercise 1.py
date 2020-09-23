print('Welcome to the Snow Board Length Counter')
feet = int(input('Please Input Your Height(feet): '))
inch = int(input('Please Input Your Height(Inch): '))
tall = (feet * 12 * 2.54) + (inch * 2.54)
board = tall * 88/100
print('Your suggested Snow Board length is',board)