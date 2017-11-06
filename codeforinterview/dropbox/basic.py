cow = set()
x = int(raw_input())
for i in range(x):
    cow.add(str(i))

line2 = raw_input().split()
n, m = int(line2[0]), int(line2[1])
share = []
confli = []
allnode = {}

for i in range(n):
    line = raw_input().split()
    k = int(line[1])
    allnode[line[0]] = set()
    for x in range(1, k + 1):
        allnode[line[0]].add(line[x + 1])
    share.append(line[0])

for i in range(m):
    line = raw_input().split()
    k = int(line[1])
    allnode[line[0]] = set()
    for x in range(1, k + 1):
        allnode[line[0]].add(line[x + 1])
    confli.append(line[0])

relation = raw_input().split()
dict = {}
for i in range(int(relation[0])):
    rela = raw_input().split()
    if rela[0] not in dict:
        dict[rela[0]] = []
    dict[rela[0]].append((rela[1]))

print dict,
res = []
for i in dict.values():
    res += i
doc = set(share+confli)
queue = list(doc - set(res))

leaves = []
while queue:
    pop = queue.pop(0)
    if pop in dict:
        for kid in dict[pop]:
            if kid in share:
                allnode[kid].update(allnode[pop])
            queue.append(kid)
    else:
        leaves.append(pop)

ans = set()
for r in leaves:
    rr = cow - allnode[r]
    if rr:
        ans.update(rr)

ans = ' '.join(sorted(list(ans)))
print ans


