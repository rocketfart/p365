import heapq

class heapnode():
    def __init__(self,name,data):
        self.name=name
        self.data = data
    def __cmp__(self, other):
        return cmp(self.data,other.data)


class solution:

    #heap hashtable
    def __init__(self):
        self.dict={}
        self.heap=[]

        self.n=0
        self.bucket=[]

    def findtopk(self,k,it):
        for i in it:
            if i not in self.dict:
                self.dict[i]=heapnode(i,1)
            else:
                self.dict[i].data+=1

        for key in self.dict.keys():
            if len(self.heap)<k:
                heapq.heappush(self.heap,self.dict[key])
            else:
                heapq.heappushpop(self.heap,self.dict[key])

        return [i.name for i in self.heap]

    def findtopkmore(self,k,it):
        for i in it:
            if i in self.dict:
                self.dict[i].data+=1
            else:
                self.dict[i]=heapnode(i,1)

            if self.dict[i].data-1<=self.heap[0].data:
                heapq.heappushpop(self.heap, self.dict[i])

        return [i.name for i in self.heap]


    def findbucket(self,k,it):

        for i in it:
            self.n+=1
            if i in self.dict:
                self.dict[i]+=1
            else:
                self.dict[i]=1

        self.buckets=[[] for i in range(self.n+1)]
        for key in self.dict:
            self.buckets[self.dict[key]].append(key)

        res=[]
        for i in range(self.n,-1,-1):
            if len(res)<k:
                res+=self.buckets[i]
            else:
                break
        return res

    def findbucketmore(self,k,it):
        newdict={}
        m=0
        for i in it:
            m+=1
            if i in newdict:
                newdict[i]+=1
            else:
                newdict[i]=1
        self.n+=m
        self.buckets+=[[] for i in range(m)]
        for key in newdict:
            self.buckets[self.dict[key]]=[]
            self.buckets[self.dict[key]+newdict[key]].append(key)

        res=[]
        for i in range(self.n-1,-1,-1):
            if len(res)<k:
                res+=self.buckets[i]
            else:
                break
        return res


case=solution()
k=2
it=iter(['1','12','21','12','21','12','21','12','21','12','21'])
print(case.findtopk(k,it))
it1=iter(['1','1','1','1','1','1','1','1','21','1','1'])
print(case.findtopkmore(k,it1))
#print(case.findbucket(k,it))
#print(case.findbucketmore(k,it1))