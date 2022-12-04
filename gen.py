import requests
import webbrowser
import time
import random

codelength = 8

list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

data = 'https://www.fortnitechapter4.com/api/codes/'

count = 0

def g(rolls):
	result = ""
	while rolls >= 1:
		c = random.choice(list)
		result = c + result
		rolls = rolls - 1
	return result

while True:


    result = f'{g(3)}-{g(2)}-{g(3)}'

    response = requests.get(f'https://www.fortnitechapter4.com/api/codes/{result}/data.json')
    if 'type' not in response:
        print(f'Code ({result}) does not work. - Attempt {count}')
        count += 1
    else:
        print(f'\nFOUND CODE!\n{result}')

        url = f'https://www.fortnitechapter4.com/api/codes/{result}'
        print(url)
        time.sleep(100000)
        exit()
