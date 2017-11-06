import bisect
import threading
class myThread():
    def __init__(self,table):
        self.lock=threading.RLock()
        self.hashtable=table
    def run(self):
        with self.lock:
            print self.hashtable

class hashtable():
    def __init__(self):
        self.map={}
    def add(self,k,v):
        self.map[k]=v
    def get(self,k):
        if k in self.map:
            return self.map[k]
        raise KeyError
    def delete(self,k):
        if k in self.map:
            return self.map.pop(k)
        raise KeyError

class hashtable2():
    def __init__(self):
        self.map=[[] for _ in 100]
        self.num=0

    def hash(self,k):
        index=k%len(self.map)
        return self.map[index]

    def add(self,k,v):
        if self.num==len(self.map):
            self.resize()
        m=self.hash(k)
        bisect.insort(m,(k,v))
        self.num+=1

    def get(self,k):
        m=self.hash(k)
        return bisect,bisect(m,k)
    def resize(self):
        newmap=[[] for _ in 2*self.num]
        for m in self.map:
            newmap[m]=self.map[m]
        self.map=newmap

def main():
    x=hashtable()

    thread1=myThread(x.add(1,2))
    thread2=myThread(x.get(1))
    thread4=myThread(x.add(2,3))
    thread3=myThread(x.delete(2))

    thread1.run()
    thread2.run()
    thread4.run()
    thread3.run()

    with lock:
        for i in work:
            queue.put(i)

    if not queue.empty():
        pass


if __name__=='__main__':
    main()