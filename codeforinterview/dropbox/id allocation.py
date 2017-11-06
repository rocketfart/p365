'''
第四轮实现两个函数，int allocate()和void release(intid)，
每调用一次allocate返回的id需要unique，为1到N之间的一个整数。
如果release以后，就可以继续被allocate。之前用array+hashmap，
达到O(1)时间和O(N)空间。后来被告知空间用得太多，map空间效率低，
最后用了bitmap。这题其实和实现文件系统的metadata区域比较类似，
不过最后居然是用时间换空间，有点让我诧异。
'''
class soluction1:
    def __init__(self,maxnum):
        self.num=set(range(maxnum))


    def get(self):
        return self.num.pop() if self.num else -1

    def release(self,num):
        if num not in self.num:
            return
        else:
            self.num.add(num)

class solution2:
    def __init__(self,maxnum):
        self.queue=range(maxnum)
        self.set=set()
        self.max=maxnum

    def get(self):
        if self.queue:
            self.set.add(self.queue[-1])
            return self.queue.pop()

    def check(self,num):
        return 0<=num<self.max and num not in self.set

    def release(self,num):
        if num not in self.set:
            return
        else:
            self.set.pop(num)
            self.queue.append(num)

from bitstring import BitArray
class solution3:
    def __init__(self,maxnum):
        #self.bitset=BitArray(maxnum)
        self.bitset=[False]*(maxnum)
        self.idx=0
        self.max=maxnum

    def get(self):
        if self.idx==self.max:
            return -1
        res=self.idx
        #self.bitset.set(1,self.idx)
        self.bitset[self.idx]=True

        # self.idx=self.bitset.find(bin(0),self.idx)
        self.idx=self.bitset.index(False, self.idx)

        return res

    def check(self,num):
        return 0<=num<self.max and not self.bitset[num]

    def release(self,num):
        if num not in self.bitset:
            return
        #self.bitset.set(0,num)
        self.bitset[num]=False
        if num<self.idx:self.idx=num


class solution4:
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