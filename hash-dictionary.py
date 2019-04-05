from hashlib import sha256
with open('dictionary.txt') as f1:
    with open('hash-dictionary.txt', 'w') as f2:
        for line in f1:
            line = str(line).replace('\n','')
            m = sha256()
            m.update(line.encode('utf-8'))
            f2.write(line + '\t' + m.hexdigest()+ '\n')