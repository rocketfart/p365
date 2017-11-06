
def find(s):

    hour,minu=s[:2],s[3:]
    nums=set([s[0],s[1],s[3],s[4]])
    nums=sorted(list(nums))

# from back to first, change num with bigger one,
# if bigger than 60 if bigger than 23 then do not do
# and change it to smallest

    allnum=list(hour+minu)

    for i in range(4)[::-1]:
        if allnum[i] != nums[-1]:
            x = nums[nums.index(allnum[i])+1]
            y = allnum[i]
            allnum[i] = x
            if i in (2,3) and ''.join(allnum[2:])<'60' and (i in (0,1) and ''.join(allnum[2:])<'24'):
                return ''.join(allnum[:2]+[':']+allnum[2:])
            allnum[i] = nums[0]
        else:
            allnum[i] = nums[0]

    return ''.join(allnum[:2]+[':']+allnum[2:])


print find('01:02')
print find('11:11')
print find('13:11')
print find('11:19')
print find('23:59')