import collections


def find(s, keypad):

    matrix=[[0]*3 for _ in range(3)]
    for x in range(3):
        for y in range(3):
            matrix[x][y]=keypad[0]
            keypad= keypad[1:]
    dict={}

    for x in range(3):
        for y in range(3):
            dict[matrix[x][y]]={}
            dict[matrix[x][y]][1]=[]
            for i in (0,1,-1):
                for j in (0,1,-1):
                    xx,yy=i+x,j+y
                    if 0<=xx<3 and 0<=yy<3:
                        dict[matrix[x][y]][1].append(matrix[xx][yy])
    res=0

    for i in range(1, len(s)):
        if s[i]!=s[i-1]:
            if s[i] in dict[s[i-1]][1]:
                res+=1
            else:
                res+=2
    return res

if __name__=='__main__':
    a=input()
    b=input()
    print find(a,b)
