import random
import threading
from multiprocessing.sharedctypes import synchronized


class loadBlancer():
    def __init__(self,dict):
        #round robin
        self.count=0
        self.lock=threading.RLock()

        self.servermap=dict
        self.itermap=iter(dict.keys())
        self.serverset=[]

    def getserver(self):
        while True:
            try:
                server=self.itermap.next()
                weight=self.servermap[server]
                for i in range(weight):
                    self.serverset.append(server)
            except:
                break
##this is how round roubin works, put a lock and index
        with self.lock:
            if self.count>=len(self.serverset):
                self.count=0
            res=self.serverset[self.count]
            self.count+=1
#this is how random works
#       res=random.choice(self.serverset)
        return res

if __name__=='__main__':
    list={'yihao':4,'erhao':1}
    x=loadBlancer(list)
    for _ in range(10):
        print x.getserver()
