def find(list, k):
    need = [range(1, len(list) + 1)]

    for day, i in enumerate(list, 1):
        for lis in range(len(need)):

            if i in need[lis]:
                index = need[lis].index(i)

                if len(need[lis][:index]) == k or len(need[lis][index + 1:]) == k:
                    return day

                need += [need[lis][:index]] + [need[lis][index + 1:]]
                need.pop(lis)
                break
    return -1


list = [2, 5, 1, 4, 3]
k = 2
print find(list, k)
