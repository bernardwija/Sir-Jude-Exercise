print('Welcome to List Converter!')
def removekeys(mydict,keylist):
    print('Here are your datas: ')
    print('Your dictionary:',mydict)
    print('Your List:',keylist)
    for i in keylist:
        if i in mydict:
            del mydict[i]
    print('Here is your new dictionary:')
    a=mydict
    return a


def dictionary():
    print('Please give us your available dictionary content down below.')
    mydict = {}
    while True:
        dict = input('Please Input The Key Name: ')
        val = input('Please Input The Key Value: ')
        mydict[dict] = val
        ans = input('Do you want to add another content(Yes or No)?: ')
        if ans == 'Yes':
            print(mydict)
            continue
        else:
            print(mydict)
            def list():
                print('Now please give us your available list content down below.')
                keylist =[]
                while True:
                    list = input('Please Input The Key Name: ')
                    keylist.append(list)
                    ans = input('Do you want to add another content(Yes or No)?: ')
                    if ans == 'Yes':
                        print(keylist)
                        continue
                    else:
                        print(keylist)
                        break
                print(removekeys(mydict,keylist))
            list()
            break
dictionary()
print('Thankyou for using our service!')









