print('Welcome to Word Counter!')
def wordfrequencies(mylist):
    dict = {}
    for i in mylist:
        dict.setdefault(i, 0)
        dict[i] = dict[i] + 1
    print('Here is your dictionary:')
    return dict

def list():
    mylist=input('Please input the sentence that you want to count: ').split()
    print(wordfrequencies(mylist))

list()
print('Thankyou for using our service!')

