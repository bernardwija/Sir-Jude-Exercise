print('Welcome to The Account Set-Up Page!')
def accept_logins(users,username,password):
    if username in users and password==users[username]:
        ans=True
        print('You have successfully loged in!')
    else:
        ans=False
        print('Your credentials are wrong.')
    return ans
def user():
    users={}
    dict = input('Please Your New Username: ')
    val = input('Please Input Your New Password: ')
    users[dict]=val
    def login():
        print('You have succesfully registered! Now please log-in!')
        username=input('Please input your username: ')
        password=input('Please input your password: ')
        print(accept_logins(users,username,password))
    login()
user()
