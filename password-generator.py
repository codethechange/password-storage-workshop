top = []
with open('top-passwords.txt') as f:
    for line in f:
        top.append(line.replace('\n',''))
words = []
from string import printable
chars = [c for c in printable if c.isalnum()]
with open('dictionary.txt') as f:
    for line in f:
        words.append(line.replace('\n',''))
from random import randint, choice
user_passwords = {'users': [], 'passwords': []}
i = 0

import pandas as pd
for _ in range(100000):
    i += 1
    user_passwords['users'].append('user' + str(i))
    num = randint(1, 100)
    if num < 25:
        password = choice(top)
        while len(password) < 6:
            password += choice(top)
        user_passwords['passwords'].append(password)
    elif num < 70:
        password = choice(words)
        while len(password) < 6:
            password += choice(words)
        user_passwords['passwords'].append(password)
    else:
        user_passwords['passwords'].append(''.join([choice(chars) for _ in range(8)]))
import json
with open('passwords.json', 'w') as f:
    json.dump(user_passwords, f)