import os
import requests
import time

ac_token = ''
message = ''
tts = 1
tts_value = ''
cid = ''

choice = int(input('What do you want to do? (0 = Send message, 1 = Quit): '))
if choice == 0:
    if os.path.exists('token.key'):
        with open('token.key', 'r') as file:
            ac_token = file.read()
            
        if ac_token == '':
            print('Invalid token in token.key')
            exit(1)
        
        print('TOKEN: {}'.format(ac_token))
           
    else:
        ac_token = input('Insert your account token: ')
        print('Is better to store your token in a \'token.key\' file. Create it?')
        create = input('[y]/n: ')
        if create.lower() == 'y' or create == '':
            with open('token.key', 'w') as file:
                file.write(ac_token)

        else:
            pass
        
    while True:
        cid = input('Insert the channel ID: ')
        message = input('Insert the text: ')
        tts = int(input('The message must be tts or not? (0 = Yes, 1 = No): '))
        if tts == 0:
            tts_value = 'true'

        elif tts == 1:
            tts_value = 'false'

        else:
            print('Insert a valid option')

        headers = {
            "authorization": f"{ac_token}"
        }

        data = {
            "content": f"{message}",
            "tts": f"{tts_value}"
        }

        url = f'https://discord.com/api/v9/channels/{cid}/messages'

        loop = int(input("Loop? (0 = Loop, 1 = Repeat, 2 = One Message): "))
        if loop == 0:
            while True:
                time.sleep(0.8)
                r = requests.post(url, data=data, headers=headers)
        if loop == 1:
            repeats = int(input('How many times? '))
            for repeat in range(repeats):
                time.sleep(0.8)
                r = requests.post(url, data=data, headers=headers)
        if loop == 2:
            r = requests.post(url, data=data, headers=headers)

elif choice == 1:
    print('See you next time!')
