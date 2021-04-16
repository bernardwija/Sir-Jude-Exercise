users = {}
memberlist = {}
current_user = []

class Bank:

    def addCustomer(self):
        print('\n''Welcome to The Bank!')
        yn = input('Do You Have an Account(answer Yes or No)?: ')
        if yn == 'No':
            print('Please Register a New Account!')
            dict = input('Please Input Your New Username: ')
            val = input('Please Input Your New Password: ')
            users[dict] = val
            if dict not in memberlist.keys():
                memberlist[dict] = 0
            Customer().setAccount()

        if yn == 'Yes':
            Customer().setAccount()


class Customer:

    def setAccount(self):
        if users == {}:
            print('No data is found, please try again.')
            Bank().addCustomer()
        else:
            print('Please log-in!')
            username = input('Please input your username: ')
            password = input('Please input your password: ')
            self.username = username
            self.password = password
            if self.username in users and self.password == users[self.username]:
                print('You have successfully loged in!')
                current_user.append(self.username)
                Account().menu()
            else:
                print('Your credentials are wrong.')
                wrong = input('Do you want to try again(Yes or No)?: ')
                if wrong == 'Yes':
                    Customer.setAccount(self)
                if wrong == 'No':
                    print('Thankyou for using our service!')


class Account:

    def menu(self):
        print('\n''Welcome Customer!')
        print('1. Balance''\n''2. Deposit''\n''3. Withdraw''\n''4. Quit')
        pick = input('Please pick a service(1,2,3,4): ')
        if pick == '1':
            Account.getBalance(self)
        if pick == '2':
            Account.deposit(self)
        if pick == '3':
            Account.withdraw(self)
        if pick == '4':
            current_user.pop(0)
            Bank().addCustomer()

    def getBalance(self):
        for a in current_user:
            for b in memberlist.keys():
                if a == b:
                    print('\n''Here is your balance: ',memberlist.get(b))
                    inp = input('Do you want to do another action(Yes or No)?: ')
                    if inp == 'Yes':
                        Account().menu()
                    if inp == 'No':
                        current_user.pop(0)
                        Bank().addCustomer()

    def deposit(self):
        amt = int(input('\n''Please enter the amount to deposit: '))
        for a in current_user:
            for b in memberlist.keys():
                if a == b:
                    memberlist[b] += amt
                    print('Here is your new balance: ', memberlist.get(b))
                    inp = input('Do you want to do another action(Yes or No)?: ')
                    if inp == 'Yes':
                        Account().menu()
                    if inp == 'No':
                        current_user.pop(0)
                        Bank().addCustomer()

    def withdraw(self):
        amt = int(input('\n''Please enter the amount to withdraw: '))
        for a in current_user:
            for b in memberlist.keys():
                if a == b:
                    if amt <= memberlist.get(b):
                        memberlist[b] -= amt
                        print('Here is your new balance: ', memberlist.get(b))
                        inp = input('Do you want to do another action(Yes or No)?: ')
                        if inp == 'Yes':
                            Account().menu()
                        if inp == 'No':
                            current_user.pop(0)
                            Bank().addCustomer()


if __name__ == "__main__":
    Bank().addCustomer()



