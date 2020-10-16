print('Welcome to Fun Translator!')
a=input('Please input a word or a sentence to translate: ')
def trans(a):
    string = ""
    for l in a:
        string += l
        if l in "bcdfghjklmnpqrstvwxz":
            string += 'o' + l
    return string
print(trans(a))
print('Thankyou for using our service!')
