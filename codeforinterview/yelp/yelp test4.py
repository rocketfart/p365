import sys

list1=['a','bb','c']
list2=['ad','xxx']

res = [[sys.maxint,'']]
for k, x in enumerate(list1):
    if x in list2:
        if res[-1][0]>k+list2.index(x):
            res=[[k+list2.index(x), x]]
print res[0][1] if res[0][0] != sys.maxint else 'Yelpwich'

