#!/usr/bin/env python3

valids = []
for number in range(11098,98123+1):
    aaa = {}
    for digit in str(number):
        aaa.setdefault(digit,0)
        aaa[digit] += 1
    
    count = aaa.get('5',0)
    if count < 2:
        continue#skip
    
    ok = False
    last = int(str(number)[0])
    for digit in str(number)[1:]:
        digit = int(digit)
        print(last, digit)
        if digit >= last:
            ok = True
        else:
            ok = False
            break
        
        last = digit
    
    if not ok:
        continue#skip
    
    valids.append(number)
    
    print(number, 'OK', ok)
    #break

print(len(valids))
print(valids[55])

#4326-13955