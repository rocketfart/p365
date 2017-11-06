def find1(list):
    m = 0
    for k, v in enumerate(list):
        if k > m:
            return False
        m = max(m, k + v)
    return True


#print find1(list=[3, 2, 1, 0, 4])
#print find1(list=[2, 3, 1, 1, 4])
print find1(list=[5, 6, 0, 4, 2, 4, 1, 0, 0, 0])


def find2(list):
    far = 0
    end = 0
    path = []
    res = True
# get max far everytime if not 0, if get next put it in path, if out of list, put 'out'
# in begining if end out of list or position bigger than far
    for k, v in enumerate(list):
        if k > far:
            return ''

        far = max(far, k + v)

        if k == end:
            path.append(str(k))
            end = far

    return ' '.join(path+['out'])


print find2(list=[5, 6, 0, 4, 2, 4, 1, 0, 0, 0])
print find2(list=[3,0])
print find2(list=[-3,0])
print find2(list=[5,1,8,0,0,1,1,1,1,1,1])


