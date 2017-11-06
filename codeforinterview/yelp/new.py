import collections
from operator import itemgetter
dict1 = [{'a':2, 'b':3,'c':4},{'a':3, 'b':4}]

counter=collections.Counter()

for d in dict1:
    counter.update(d)

x=collections.defaultdict(list)
x[1].append({1:2})
x[1].append({3:3})
#dict={{"session 1": {"burger": 1, "sandwich": 2}}, {"session 2": {"burger": 3, "water": 2}}, {"session 1": {"burger": 3, "water": 1}}}
#dict2={"session 1", [{"burger", 1, "sandwich", 2}]}, {"session 2", {"burger", 3, "water", 2}}, {"session 1", {"burger", 3, "water", 1}}
d={
"employees": [
{ "session 1":[{"burger", 1, "sandwich", 2}] },
{ "session 2":[{"burger", 4, "sandwich", 2}]},
{ "session 1":[{"burger", 1, "water", 2}] }
]
}
d = {1: 2, 3: 4, 5: [{7: {9: 1}}]}
print type(d)
def get_keys(dl, keys_list):
    if isinstance(dl, dict):
        keys_list += dl.keys()
        map(lambda x: get_keys(x, keys_list), dl.values())
    elif isinstance(dl, list):
        map(lambda x: get_keys(x, keys_list), dl)
list1=[]
get_keys(d,list1)
x={'water': 5, 'burger': 2, 'sandwich': 2}
for i in x.items():
    print i[0]
x=collections.OrderedDict(sorted(x.items(),key= lambda x:x[1]))

list=['a','b','c']
list2=['a','b']
print [a+b for a in list for b in list2]
div,mod=divmod(4,5)
print mod