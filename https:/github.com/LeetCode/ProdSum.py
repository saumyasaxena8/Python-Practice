num = 324
s = str(num)
add = 0
mult = 1
for i in range(len(s)):
    add += int(s[i])
    mult *= int(s[i])
    +i
print(add)
print(mult)
res = mult - add
print('Result',res)
