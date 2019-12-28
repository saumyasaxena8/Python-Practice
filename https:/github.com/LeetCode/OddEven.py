nums = [12,5,988,6767,23,1,45,54545454,555,67]
lst = []
c = 0
for i in nums:
    if len(str(i)) % 2 == 0:
        c += 1
print('Number of Even Digits:', c)