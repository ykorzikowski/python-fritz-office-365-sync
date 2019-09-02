from radiator_fritz_o365_sync.core import Core


def print_out_token():
    with open('o365_token.txt', 'r') as fin:
        print(fin.read())

if __name__ == "__main__":
    account = Core.get_account()
    print("Starting authentication process...")
    print("Please visit the following url and paste the result url into the cli!")
    account.authenticate(scopes=Core.get_scopes())

    print('Make sure this file is located in /usr/src/app/o365_token.txt')
    print_out_token()
