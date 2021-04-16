print('Welcome to Letter Counter!')
def char_freq(string):
    list={}
    for m in string:
        if m not in list:
            list[m] = 1
        else:
            list[m] += 1
    return list

def member():
    string = input('Please input a word or a sentence to count: ')
    print('Your Message: ', string)
    print('Here are your letter frequencies:',char_freq(string))
    print('Thankyou for using our service!')
member()