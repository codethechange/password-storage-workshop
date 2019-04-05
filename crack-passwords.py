
# Load table
dictionary_table = {}
with open('hash-dictionary.txt', 'r') as f:
    for line in f:
        password, hash_value = tuple(line.split('\t'))
        dictionary_table[hash_value.replace('\n','')] = password.replace('\n', '')
# See if we can crack any passwords
import json
with open('hashed-passwords.json') as f:
    d = json.load(f)
cracked_users = []
for i in range(len(d['users'])):
    if d['passwords'][i] in dictionary_table: # the hash exists! We have found a collision
        cracked_users.append((d['users'][i], dictionary_table[d['passwords'][i]]))
print('Cracked ' + str(len(cracked_users)) + ' passwords!')
print(cracked_users[-10:])
