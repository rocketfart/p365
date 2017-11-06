
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:return 0
        res=0
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    queue=[(i,j)]
                    grid[i][j]='0'

                    while queue:
                        a,b=queue.pop(0)
                        for x,y in (1,0),(0,1),(-1,0),(0,-1):
                            xx,yy=a+x,b+y
                            if 0<=xx<m and 0<=yy<n and grid[xx][yy]=='1':
                                queue.append((xx,yy))
                                grid[xx][yy]='0'
                    res+=1
        return res

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            grid[i][j] = '0'
            if i + 1 < m and grid[i + 1][j] == '1':
                dfs(i + 1, j)
            if j + 1 < n and grid[i][j + 1] == '1':
                dfs(i, j + 1)
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                dfs(i - 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        uf = unionfind(grid)
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for x, y in (1, 0), (-1, 0), (0, 1), (0, -1):
                        xx, yy = x + i, y + j
                        if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                            a, b = i * n + j, xx * n + yy
                            uf.union(a, b)
        return uf.size


class unionfind():
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.father = [0] * m * n
        self.size = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    id = i * n + j
                    self.father[id] = id
                    self.size += 1

    def union(self, a, b):
        find1 = self.find(a)
        find2 = self.find(b)
        if find1 != find2:
            self.father[find1] = find2
            self.size -= 1

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

friends = []
size = []

def root(a):
        i = a
        while(friends[i] != i):
                i = friends[i]
        return i

def find(a, b):
        if(root(a) == root(b)):
                friends[a] = friends[friends[a]]
                return True
        return False

def union(a, b):
        i = root(a)
        j = root(b)
        if(size[i] < size[j]):
                size[j] += size[i]
                friends[i] = j
        else:
                size[i] += size[j]
                friends[j] = i

def cntset():
        setcnt = 0
        for i in range(peoplecnt):
                if(friends[i] == i):
                        setcnt += 1
        return setcnt


peoplecnt = int(raw_input("Input Number of people:"))
for i in range(peoplecnt):
        friends.append(i)
        size.append(1)
while True:
        a = int(raw_input("Input a:"))
        b = int(raw_input("Input b:"))
        if(a == -1 | b == -1):
                break;
        else:
                union(a,b)
print(cntset())
