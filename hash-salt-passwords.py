import json
with open('passwords.json') as f:
    d = json.load(f)
from string import printable
chars = [c for c in printable if c.isalnum()]
for i in range(len(d['users'])):
    pass # TODO
with open('salted-passwords.json', 'w') as f:
    json.dump(d,f)