
# Load table
words = []
with open('dictionary.txt') as f:
    for line in f:
        line = str(line).replace('\n','')
        words.append(line)
# See if we can crack any passwords
import json
with open('salted-passwords.json') as f:
    d = json.load(f)
cracked_users = []
from hashlib import sha256
for i in range(len(d['users'])):
    pass # TODO
print('Cracked ' + str(len(cracked_users)) + ' passwords!')
print(cracked_users[-10:])
