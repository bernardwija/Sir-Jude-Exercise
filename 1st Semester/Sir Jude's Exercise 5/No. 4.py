print('Welcome to List Checker!')
def is_member(x, a):
    for m in range(len(a)):
        if x == a[m]:
            return True
    return False

def member():
    x=input('Please input the character you want to check: ')
    a =input('Please input your list characters seperated by space: ').split()
    print('Here is your list:',a)
    print(is_member(x,a))
    print('Thankyou for using our service!')

member()
