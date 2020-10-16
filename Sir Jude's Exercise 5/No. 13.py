print('Welcome to English Class: ')
def english(data):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if data.endswith('ie'):
        if True:
            data = data[:-2]
            a = data + "ying"
            return a
    if data.endswith('e'):
        if True:
            data = data[:-1]
            b = data + "ing"
            return b
    if data[-1] not in vowels:
        if data[-2] in vowels:
            if data[-3] not in vowels:
                c = data + str(word[-1]) + "ing"
                return c
    return data += 'ing'

def member():
    data = input("Please input your word: ")
    print(english(data))
    print('Thankyou for using our service!')
member()
