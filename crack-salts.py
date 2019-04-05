
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
    salt, hash_val = tuple(d['passwords'][i].split('$'))
    if i % 10 == 0:
        print(i)
    # Generate salted hash for each word
    for word in words:
        m = sha256()
        m.update(str(salt + word).encode('utf-8'))
        if m.hexdigest() == d['passwords'][i]: # the hash exists! We have found a collision
            cracked_users.append((d['users'][i], word))
            break
print('Cracked ' + str(len(cracked_users)) + ' passwords!')
print(cracked_users[-10:])
