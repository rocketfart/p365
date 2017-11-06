import collections

list=['red','black','green','white','red','black','black','red']

res=[]
dict=collections.Counter(list)

max=max(dict.values())
for k,v in dict.items():
	if v==max:
		res.append(k)
print res
