'''
Bri Harris's main.py file
'''


menu = '''Menu
-------------
1. Encode
2. Decode
3. Quit
    '''


store = ''


def encode(password):
    encoded_secret = ''
    for c in password:
        if int(c) > 6:
            encoded_secret += str(int(c) + 3)[1]
        else:
            encoded_secret += str(int(c) + 3)
    return encoded_secret


def decode(password):
    decoded_secret = ''
    for c in password:
        if int(c) < 3:
            decoded_secret += str(int(c) + 10 -3)
        else:
            decoded_secret += str(int(c) - 3)
    return decoded_secret


if __name__ == '__main__':
    while True:
        print(menu)
        selection = int(input('Please enter an option: '))
        if selection == 1:
            store = encode(input('Please enter the password to encode: '))
            print('Your password has been encoded and stored!\n')
        elif selection == 2:
            # if store is None:
            #     print('Enter a password to encode first')
            # else:
            print(f'The encoded password is {decode(store)}, and the original password is {store}.\n')
        elif selection == 3:
            break