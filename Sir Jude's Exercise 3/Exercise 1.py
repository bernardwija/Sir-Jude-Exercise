print('Welcome to The Day Counter!')
def convert_to_days():
    a = float(input('Please Input Amount of Hours: '))
    b = float(input('Please Input Amount of Minutes: '))
    c = float(input('Please Input Amount of Seconds: '))
    h = a * 3600
    m = b * 60
    s = c * 1
    day = (h+m+s)/86400
    return day

def get_days():
    print('Your Total Number of Days is:',round(convert_to_days(),4))
get_days()




