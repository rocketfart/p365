import math

list1=[[5,7,7],
       [7,5,8],
       [9,1,5]]
list=[[3,1,2,4],
      [5,7,1,8],
      [3,9,2,6]]

#Idea: Use DP dp[r][c] = min(max(dp[r-1][c-1], dp[r][c-1], dp[r+1][c-1]), grid[r][c]
def find(list):

    m,n=len(list),len(list[0])
    dp=[[0]*(n) for _ in range(m)]
    for i in range(m):
        dp[i][0] = list[i][0]

    for i in range(m):
        for j in range(1,n):
            minx = dp[i][j-1]
            if i-1 >= 0:
                minx = max(minx,dp[i-1][j-1])
            if i+1 < m:
                minx = max(minx,dp[i+1][j-1])
            dp[i][j]=min(minx,list[i][j])

    return max(dp[i][n-1] for i in range(m))

def find1(list):
    m,n=len(list),len(list[0])
    dp=[0]*m

    for i in range(m):
        dp[i]=list[i][0]

    for j in range(1,n):
        newdp = [0] * m
        for i in range(m):
            newdp[i]=dp[i]
            if i-1>=0:
                newdp[i]=max(newdp[i],dp[i-1])
            if i+1<m:
                newdp[i]=max(newdp[i],dp[i+1])
            newdp[i]=min(newdp[i],list[i][j])
        dp[:]=newdp

    return max(dp)

print (find1(list))

