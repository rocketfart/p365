import collections


def recomment(graph1,graph2,target):
    dict={}
    res=[]
    targetSet=set()

    for a,b in graph1:
        if a == target:
            targetSet.add(b)

    for x,y in graph2:
        if x in targetSet:
            dict[y].append(x)

    for k,v in dict:
        if len(v)>=4:
            res.append(k)

    return sorted(res)

new_res=collections.defaultdict(list)
for k,v in res:
    if k in new_res:
        for a, b in new_res[k]:
            if a == v[0]:
                a += v[1]
            if a != v[0] and a not in new_res[k]:
                new_res[k].append(v)
    else:
        new_res.append(v)