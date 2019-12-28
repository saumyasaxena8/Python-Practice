address = '12.89.444.00'
test = []
for i in address:
    if i == '.':
        test = address.replace('.','[.]')
print(test)