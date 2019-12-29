J = 'z'
S = 'ZZ'
c = 0
for i in S:
    print(i,'its the for loop')
    if i in J:
        print(i,'its the if')
        c += 1
print(c)