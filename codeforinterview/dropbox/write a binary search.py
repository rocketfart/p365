# coding=utf-8
l,r,target=0,9,5
num=[0,1,2,5,5,5,6,7,8,9]
# 不出死循环 如果是1，2 则卡死
while l+1<r:
    mid=(l+r)//2
    if num[mid]==target:
        r=mid
    elif num[mid]<target:
        l=mid
    else:
        r=mid
print l,r

#if find first position like upon
#if find last l=mid
#find fist smaller or bigger than something, can not +=1
# 最后缩减到两个数字

# <n  n**1/2 log n 1


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    l,r=0,x
    if x==0:return 0
    if x==1:return 1
    while l+1<r:
        mid=(l+r)//2
        if mid*mid<=x<(mid+1)*(mid+1):
            return mid
        elif mid*mid<x:
            l=mid
        else:
            r=mid
    return -1

def mysqrt2(x):
    l,r=1,x/2+1
    while l<=r:
        mid=(l+r)//2
        if mid*mid<=x<(mid+1)*(mid+1):
            return mid
        elif mid*mid<x:
            l=mid
        else:
            r=mid
    return -1

def sqrbool(x):
    l,r=1,x/2+1
    while l+1<r:
        mid=(l+r)//2
        if mid*mid==x:
            return True
        elif mid*mid<x:
            l=mid
        else:
            r=mid
    return False
print mysqrt2(2)
#如果只是判断有没有int 就用l+1<r 并且不+=1
#如果要把近似值找出来，如果想写在一起 就要用叠加lr