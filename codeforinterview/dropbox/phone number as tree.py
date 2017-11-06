class solution3:
    def __init__(self,maxnum):
        self.tree=[True]*2*maxnum
        self.m=len(self.tree)
        self.max=maxnum

    def get(self):
        if self.tree[1]==False: return -1
        i=1
        while i<self.m/2:
            if 2*i<self.m and self.tree[2*i]:
                i=2*i
            if 2*i+1<self.m and self.tree[2*i+1]:
                i=2*i+1

        ret=i-self.max

        self.tree[i]=False

        i/=2
        while i>0:
            self.tree[i]=self.tree[2*i] or self.tree[2*i+1]
            i/=2
        return ret

    def check(self,number):
        return 0<=number<self.m and self.tree[number+self.max]

    def release(self,number):
        i= self.max+number
        while i>0:
            self.tree[i]=True
            i/=2