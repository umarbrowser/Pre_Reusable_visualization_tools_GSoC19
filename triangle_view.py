import sys

np_map = 'on'
np_loc = 'off'
acc_grant = True
Pwd = '~/Home/User/'

class Config():
    def __init__(self):
        self.user = input('Enter Your Alias: ')
        self.full_name = input('Enter Your Full Name: ')
        self.Org = input('Provide Your Organisation of Google Summer of Code 2019 ')

    def user(self):
        name = self.user
        full_name = self.full_name
        organisation = self.Org

        try:
            if name != 'PYC0D3R'.lower() | full_name != 'UMAR HARUNA ABDULLAHI'.lower() | organisation != 'incf'.upper():
                print('[-] Error 202')

            else:
                print('[+] Access Granted')

        except name == '' | full_name == '' | organisation == '':
            print('[-] Empty Input')
            sys.exit(10)

if __name__ == '__main__':
    user = Config()
    user()