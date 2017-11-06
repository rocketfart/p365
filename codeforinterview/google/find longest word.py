import collections
wordlist=['a','aa','ab','aaa','aab','aabb']
def find(wordlist):
    dict=collections.defaultdict(list)
    for i in wordlist:
        dict[len(i)].append(i)
    key=max(dict.keys())

    def dfs(idx,x):
        if idx==0:
            return True
        for i in dict[idx]:
            if i in x:
                return dfs(idx-1,i)
        return False

    while key:
        for i in dict[key]:
           if dfs(key-1,i):
               return i
        key-=1
    return 0

print(find(wordlist))