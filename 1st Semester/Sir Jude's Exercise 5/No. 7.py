print('Welcome to Word Counter!')
def counter(word):
    result = []
    for m in range(len(word)):
        result.append(len(word[m]))
    return result
def member():
    word = [str(x) for x in input("Please enter the word you want to count: ").split()]
    print("Your word list: ", word)
    print("Your word length: ", counter(word))
    print('Thankyou for using our service!')
member()