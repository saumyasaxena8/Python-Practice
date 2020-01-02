s1 = input('enter string 1:')
s2 = input('enter string 2:')
s1.replace(' ','').lower()
s2.replace(' ','').lower()

if len(s1) != len(s2):
    print('False')

count = {}

for letter in s1:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

for letter in s2:
    if letter in count:
        count[letter] -= 1
    else:
        count[letter] = 1

for k in count:
    if count[k] != 0:
        print('False')

print('True')