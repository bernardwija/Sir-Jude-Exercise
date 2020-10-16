print('Welcome to List Checker!')
def overlap(lst1, lst2):
    x=input('Please input the character you want to check: ')
    for m in range(len(lst1)):
        if x==lst1[m] and x==lst2[m]:
            return True
    return False
def member():
    lst1 = input('Please input your list1 characters seperated by space: ').split()
    lst2 = input('Please input your list2 characters seperated by space: ').split()
    print('Here is your ls1 list:',lst1)
    print('Here is your ls2 list:',lst2)
    print(overlap(lst1,lst2))
    print('Thankyou for using our service!')
member()

