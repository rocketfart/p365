def find(limit):
    for i in range(0, 10):
        dfs(i, i, 1, limit)


def dfs(sum, i, lev, limit):
    for x in ((i - 1), (i + 1)):
        res = sum + (x * (10 ** lev))
        if 0<res <= limit:
            if x!=0:
                print res
            dfs(res, x, lev + 1, limit)

find(1000)