import random


class loadBalancer():

    def __init__(self,list):
        self.serverdict=list
        self.iterator=iter([i[0] for i in self.serverdict])
        self.serverlist=[]

    def getserver(self):
        while True:
            try:
                server=self.iterator.next()
                weight=[i[1] for i in self.serverdict if i[0]==server]
                for i in range(weight[0]):
                    self.serverlist.append(server)
            except:
                break
        res=random.choice(self.serverlist)
        return res

if __name__=='__main__':
    list=[('yihao',4),('erhao',1)]
    print loadBalancer(list).getserver
