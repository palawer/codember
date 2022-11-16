#!/usr/bin/env python3

text = '11610497110107115 102111114 11210897121105110103 9911110010110998101114 11210810197115101 11510497114101'

decrypted_words = []
for word in text.split(' '):
    code = ''
    decrypted_word = ''
    for digit in word:
        code += digit
        if int(code)>=97:
            decrypted_word += chr(int(code))
            code = ''
    
    decrypted_words.append(decrypted_word)

print(' '.join(decrypted_words))
