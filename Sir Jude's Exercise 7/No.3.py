def findvalue(mydict,val):
    print('Here are your datas: ')
    print('Your dictionary:', mydict)
    print('Your List:', val)
    print('Here is your dictionary: ')
    keys=[]
    for key,value in mydict.items():
        for i in val:
            if i == value:
                keys.append(key)
    return keys
def dictionary():
    print('Please give us your available dictionary content down below.')
    mydict = {}
    while True:
        dict = input('Please Input The Key Name: ')
        var = input('Please Input The Key Value: ')
        mydict[dict] = var
        ans = input('Do you want to add another content(Yes or No)?: ')
        if ans == 'Yes':
            print(mydict)
            continue
        else:
            print(mydict)
            def variable():
                print('Now please give us your available variable list down below.')
                val =[]
                while True:
                    list = input('Please Input The Variable: ')
                    val.append(list)
                    ans = input('Do you want to add another variable(Yes or No)?: ')
                    if ans == 'Yes':
                        print(val)
                        continue
                    else:
                        print(val)
                        break
                print(findvalue(mydict,val))
            variable()
            break
dictionary()
print('Thankyou for using our service!')