def figureKey(a='Atvt hrqgse, Cnikg', b='Your friend, Alice'):
    keySet = []
    a.lower()
    b.lower()

    for j in range(len(a)):
        if a[j].isalpha():
            if ord(a[j]) < ord(b[j]):
                keySet.append(abs(ord(a[j]) + 26 - ord(b[j])))
            else:
                keySet.append(ord(a[j]) - ord(b[j]))

    for j in range(1, len(keySet)):
        n = len(keySet) / j
        m = len(keySet) % j
        tmp = []
        tmp += (keySet[:j]) * n
        if m and keySet == tmp+ keySet[-m:] or (not m and keySet == tmp):
            keySet[:j] * 2

    print [keySet[i:i + 7] for i in range(7)]



def func(a, key):
    b = list(a)
    j = 0

    for i in range(len(b)):

        if b[i].isalpha():
            b[i] = chr(ord(b[i]) - int(key[j % len(key)]))
            if a[i].upper() == a[i] and b[i] < 'A':
                b[i] = chr(ord(b[i]) + 26)
            elif a[i].upper() != a[i] and b[i] < 'a':
                b[i] = chr(ord(b[i]) + 26)
            j += 1

    return ''.join(b)


if __name__ == '__main__':
    a1 = 'Atvt hrqgse, Cnikg'
    a = 'Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg'
    b = 'Your friend, Alice'

    key=[8,2,5,1,2,2,0]
    print func(a, key)


