import requests
import random

list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

data = 'https://www.fortnitechapter4.com/api/codes/'

count = 0
while True:
    result = ''
    for i in range(9):
        pr = random.choice(list)
        result += pr

    response = requests.get(f'https://www.fortnitechapter4.com/api/codes/{result}/data.json')
    if 'type' not in response:
        print(f'Code ({result}) does not work. - Attempt {count}')
        count += 1
    else:
        print(f'\nFOUND CODE!\n{result}')
        exit()
