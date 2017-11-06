def find(num):
    map=[0]*257

    for i in range(len(map)):
        map[i]=bin(i).count('1')

    sum=0
    while num:
        m=num&255
        sum+=map[m]
        num>>=8

    return sum

print find(12)
print bin(12)