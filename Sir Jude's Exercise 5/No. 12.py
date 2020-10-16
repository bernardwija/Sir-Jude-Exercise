print('Welcome to Verb Changer!')
def translate(data,a,b,c):
    for m in a:
        if m in data[-2:]:
            result=data+'es'
            return result
    for m in b:
        if m in data[-1:]:
            result=data+'es'
            return result
    for m in c:
        if m in data[-1:]:
            result=data[0:-1:]+'ies'
            return result
    result=data+'s'
    return result
def member():
    data=input('Please input the verb you want to change: ')
    a=['ch','sh']
    b=['o','s','x','z','y']
    c=['y']
    print('Your Original Verb: ',data)
    print('Your Changed Verb: ',translate(data,a,b,c))
    print('Thankyou for using our service!')
member()