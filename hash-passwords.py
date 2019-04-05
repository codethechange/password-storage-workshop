import pandas as pd
from hashlib import sha256
import json
with open('passwords.json') as f:
    d = json.load(f)
for i in range(len(d['users'])):
    m = sha256()
    m.update(str(d['passwords'][i]).encode('utf-8'))
    d['passwords'][i] = m.hexdigest()
with open('hashed-passwords.json', 'w') as f:
    json.dump(d,f)