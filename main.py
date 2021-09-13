import requests
import time

main_loop = True
main_repeat = 0
while main_loop:
    if main_repeat >= 3:
        lcont = int(input('Continue? (0 = Yes, 1 = No)'))
    elif main_loop < 3:
        lcont = int(input('What do you want to do? (0 = New message, 1 = Quit): '))
        if lcont == 1:
            print('See you next time!')
            break
        if lcont == 0:
            ac_token = input('Insert your accout token: ')
            cid = input('Insert the channel id: ')
            message = input("What's the message? ")
            tts = int(input('Use vocal chat? (0 = Yes, 1 = No): '))
            while True:
                if tts == 0:
                    tts_value = 'true'
                    break
                elif tts == 1:
                    tts_value = 'false'
                    break
                else:
                    print('Insert a valid character')
                    pass
            loop = int(input("Loop? (0 = Loop, 1 = Repeat, 2 = One Message): "))

            if loop == 0:
                while True:
                    headers = {
                        "authorization": f"{ac_token}"
                    }

                    data = {
                        "content": f"{message}",
                        "tts": f"{tts_value}",
                    }

                    r = requests.post(f'https://discord.com/api/v9/channels/{cid}/messages', data=data, headers=headers,)
            elif loop == 1:
                repeats = int(input('How many times? '))
                for repeat in range(repeats):
                    time.sleep(0.8)
                    headers = {
                        "authorization": f"{ac_token}"
                    }

                    data = {
                        "content": f"{message}",
                        "tts": f"{tts_value}",
                    }

                    r = requests.post(f'https://discord.com/api/v9/channels/{cid}/messages', data=data, headers=headers, )
            elif loop == 2:
                headers = {
                    "authorization": f"{ac_token}"
                }

                data = {
                    "content": f"{message}",
                    "tts": f"{tts_value}",
                }

                r = requests.post(f'https://discord.com/api/v9/channels/{cid}/messages', data=data, headers=headers, )
                main_repeat = main_repeat + 1
