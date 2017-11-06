# coding=utf-8
a = 'eeeestreeee1'
newstring = list(a)
res = []
# 不是e就放res，是就开始计数，1放在res，大于1就继续，不是e继续变成0
count = 0

for i in newstring:
    if i != 'e':
        count = 0
        res.append(i)
    else:
        count += 1
        if count == 1:
            res.append(i)
        if count > 1:
            continue

print ''.join(res)
