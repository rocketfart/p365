import collections

strq = " Sam, Ian, technical lead, 2009/ lam, Ian, technical lead, 2008/ Ian, NULL, CEO, 2007/ Fred, Sam, developer, 2010"

#
def treeEmployee(strq):

    strq = strq.split('/')
    relations = [i.split(',') for i in strq]
    graph = collections.defaultdict(list)
    namelist = {}
    start = ''
    res = []

    for i in relations:
        namelist[i[0]] = i[0] + ''.join(i[2:])
        if i[1] == ' NULL':
            start = i[0]
            continue
        graph[i[1]].append(i[0])

    def dfs(level, person):
        res.append((level, person))

        for i in graph[person]:
            dfs(level + 1, i)

    dfs(0, start)

    for i in res:
        print '-' * i[0] + ''.join(namelist[i[1]]).strip()


treeEmployee(strq)