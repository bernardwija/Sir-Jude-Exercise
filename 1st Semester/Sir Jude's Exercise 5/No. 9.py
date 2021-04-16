print('Welcome to Word Filter!')
def filter_long_words(Iword):
    result = []
    for m in range(len(Iword)):
        if (len(Iword[m])>4):
            result.append(Iword[m])
    return result
def member():
    Iword = [str(x) for x in input('Please enter the word(s) you want to filter seperated by space: ').split()]
    print("Your word list: ", Iword)
    print("Your eligible word(s): ", filter_long_words(Iword))
    print('Thankyou for using our service!')
member()