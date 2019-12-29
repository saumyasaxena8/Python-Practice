num = 324
ls = []
ls.append(num)
add = 0
mult = 1
for i in range(len(ls)):
    add += int(ls[i])
    mult *= int(ls[i])
    +i
print(add)
print(mult)
res = mult - add
print('Result',res)