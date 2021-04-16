print('Welcome to Star Printer!')
def histogram(lst):
    for m in lst:
        result = print('*' * m)
    return result
def member():
    lst = [int(data) for data in input("Please input your list characters seperated by space: ").split()]
    print(lst)
    histogram(lst)
    print('Thankyou for using our service!')
member()

