
def find(s):
    n=len(s)
    dp=[[0]*n for _ in range(n)]
    p=[[False]*n for _ in range(n)]

    for i in range(n):
        p[i][i]=True
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=1
            p[i][i+1]=True

    for gap in range(2,n):
        for x in range(n-gap):
            y=x+gap
            if s[x]==s[y] and p[x+1][y-1]==True:
                p[x][y]=True
            if p[x][y]==True:
                dp[x][y]=dp[x+1][y]+dp[x][y-1]+1-dp[x+1][y-1]
            else:
                dp[x][y]=dp[x+1][y]+dp[x][y-1]-dp[x+1][y-1]
    return dp[0][n-1]

s="abbaeae"
print find(s)
