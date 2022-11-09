#!/usr/bin/env python3

required_keys = {
    'usr',#nombre de usuario
    'eme',#email
    'psw',#contraseña
    'age',#edad
    'loc',#ubicación
    'fll',#número de seguidores
}

correct_users = []
with open('./users.txt', 'r') as fp:
    user_line = []
    for line in fp.readlines():
        ln = line.rstrip()
        
        if not ln:
            joined_line = ' '.join(user_line)
            
            keys = set()
            key_value = {}
            for pair in joined_line.split(' '):
                key, value = pair.split(':')
                key_value[key] = value
                keys.add(key)
            
            diff = required_keys-keys
            if not diff:
                correct_users.append(key_value)
            
            user_line = []
            continue#skip
        else:
            user_line.append(ln)

print(len(correct_users))
print(correct_users[-1])
