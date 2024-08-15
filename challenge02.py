#!/usr/bin/env python3

text = '116561181061045651505752561029911097108'

decrypted_words = []
for word in text.split(' '):
    code = ''
    decrypted_word = ''
    for digit in word:
        code += digit
        if int(code)>=48:
            decrypted_word += chr(int(code))
            code = ''
    
    decrypted_words.append(decrypted_word)

print(' '.join(decrypted_words))
