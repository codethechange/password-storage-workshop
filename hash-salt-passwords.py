import pandas as pd
from hashlib import sha256
import hashlib, binascii
import json
from secrets import choice
with open('passwords.json') as f:
    d = json.load(f)
from string import printable
chars = [c for c in printable if c.isalnum()]
for i in range(len(d['users'])):
    salt = ''.join([choice(chars) for _ in range(8)])
    val = binascii.hexlify(hashlib.hmac('sha256', d['passwords'][i].encode('ascii'), salt.encode('ascii'), 1000000))
    d['passwords'][i] = salt + '$' + val.decode('ascii')
    print(d['passwords'][i])
with open('salted-passwords.json', 'w') as f:
    json.dump(d,f)