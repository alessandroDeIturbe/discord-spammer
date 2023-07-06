import os
import requests
import time


def get_token():
    if os.path.exists('token.key'):
        with open('token.key', 'r') as file:
            token = file.read().strip()

        if not token:
            print('Invalid token in token.key')
            exit(1)

    else:
        token = input('Insert your account token: ')
        print('It is better to store your token in a \'token.key\' file. Create it?')
        create = input('[y]/n: ')
        if create.lower() == 'y' or create == '':
            with open('token.key', 'w') as file:
                file.write(token)

    return token


def send_message(token, channel_id, message, tts):
    headers = {
        "authorization": token
    }

    data = {
        "content": message,
        "tts": str(bool(tts))
    }

    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(str(e))
        print('Stopping process for 10 seconds...')
        time.sleep(10)


def main():
    token = get_token()
    choice = int(
        input('What do you want to do? (0 = Send message, 1 = Quit): '))

    if choice == 0:

        channel_id = input('Insert the channel ID: ')
        message = input('Insert the text: ')
        tts = int(input('Should the message be TTS or not? (0 = Yes, 1 = No): '))
        loop = int(input("Loop? (0 = Loop, 1 = Repeat, 2 = One Message): "))

        if loop == 0:
            while True:
                try:
                    send_message(token, channel_id, message, tts)
                    print('Message sent successfully!')
                except Exception as e:
                    print('Failed to send message:', str(e))
        else:
            repeats = int(input('How many times? ')) if loop == 1 else 1
            for _ in range(repeats):
                time.sleep(0.8)

                try:
                    send_message(token, channel_id, message, tts)
                    print('Message sent successfully!')
                except Exception as e:
                    print('Failed to send message:', str(e))

    elif choice == 1:
        print('See you next time!')


if __name__ == '__main__':
    main()
