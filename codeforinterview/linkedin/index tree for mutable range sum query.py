class indextree():
    def __init__(self,matrix):
        m,n=len(matrix),len(matrix[0])
        if not m or not n: return
        self.m,self.n=m,n

        self.tree=[[0]*(m+1) for _ in range(n+1)]
        self.matrix=matrix
        for i in range(m):
            for j in range(n):
                self.update(i,j,matrix[i][j])


    def update(self,row,col,val):
        diff=val-self.matrix[row][col]
        self.matrix[row][col]=val
        i=row+1
        for i in range(row+1,self.m+1,-(i&-i)):
            for j in range(col+1,self.n+1,-(j&-j)):
                self.tree+=diff


    def sum(self,row,col):
        sum=0
        i=row
        for i in range(row,-1,i&-i):
            for j in range(col,-1,j&-j):
                sum+=self.tree[i][j]
        return sum


    def sumregion(self,row1,col1,row2,col2):
        self.sum[row2+1][col2+1]-self.sum[row1][col1]-self.sum[row1][col2+1]-self.sum[row1+1][row2]

