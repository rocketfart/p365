class solution:
    def find1(self,list,target):
        res=[]
        def help(idx,tmp,count):
            if count == target:
                res.append(tmp)
                return
            elif count>target:
                return
            else:
                for i in range(idx,len(list)):
                    help(i,tmp+[list[i]],count+list[i])
        help(0,[],0)
        return res

    def find2(self, list1, target):
        list2=set(list1)
        list1=list(list2)
        list1.sort()

        dp=[]
        for i in range(target+1):
            ndp=[]
            for j in range(len(list1)):
                if list1[j]>i:
                    break
                elif list1[j]==i:
                    ndp.append([i])
                else:
                    ndp.extend(x + [list1[j]] for x in dp[i - list1[j]] if x[-1] <= list1[j])

            dp.append(ndp)

        return dp[-1]

list=[1,1,6,2]
target=12
case=solution()
#print ('1',sorted(case.find1(list,target)))
print ('2',sorted(case.find2(list,target)))