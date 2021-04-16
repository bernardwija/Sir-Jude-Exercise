print('Welcome to Word Counter!')
def find_longest_word(Iwords):
    Iwords.sort(key=len)
    result=len(Iwords[-1])
    return result
def member():
    Iwords = [str(x) for x in input("Please enter the words you want to count seperated by space: ").split()]
    print("Your word list: ", Iwords)
    print("Your longest word length: ", find_longest_word(Iwords))
    print('Thankyou for using our service!')
member()
