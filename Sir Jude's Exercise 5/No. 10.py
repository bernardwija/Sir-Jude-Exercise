print('Welcome to Letter Checker!')
def check(x,a):
    for m in a:
        if m not in x:
            print('This word or sentence is not a panagram!')
            return False
    print('This word or sentence is a panagram!')
    return True
def member():
    x=input('Please input a word or a sentence to translate: ')
    a ='abcdefghijklmnopqrstuvwxyz'
    print('All English Alphabet: ',a)
    print(check(x,a))
    print('Thankyou for using our service!')
member()


