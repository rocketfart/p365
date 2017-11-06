import collections
def gameOfLife(board):
    m, n = len(board), len(board[0])

    #newboard=[['0']*n for _ in m]

    def help(i, j):
        count = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < m and 0 <= y < n and (x!=i or y!=j) and (board[x][y] == 'x' or board[x][y] == '2'):
                    count += 1
        return count

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'x':
                if not (help(i, j) == 2 or help(i, j) == 3):
                    board[i][j] = '2'
                    # newboard='0'
            else:
                if help(i, j) == 3:
                    board[i][j] = '3'
                    # newboard='x'

    for i in range(m):
        for j in range(n):
            if board[i][j] == '3':
                board[i][j] = 'x'
            elif board[i][j] == '2':
                board[i][j] = '0'
    # return newboard


def gameOfLife1(board):
    def gameOfLifeInfinite(live):

        ctr=collections.Counter((x,y) for i,j in live
                                 for x in range(i-1,i+2)
                                 for y in range(j-1,j+2)
                                 if x!=i or y!=j)

        return {c for c in ctr if ctr[c]==3 or (ctr[c]==2 and c in live)}

    live = [(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live == 'x']
    live = gameOfLifeInfinite(live)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i,j) in live:
                board[i][j] = 'x'
            else:
                board[i][j] = '0'
                #row[j] = int((i, j) in live)


def gameOfLife2(board):
    m, n =3, len(board[0])

    newboard=board[1]

    def help(i, j):
        count = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < m and 0 <= y < n and (x != i or y != j) and (board[x][y] == 'x'):
                    count += 1
        return count

    for j in range(n):
        if board[1][j] == 'x':
            if not (help(1, j) == 2 or help(1, j) == 3):
                newboard[j]='0'
        else:
            if help(1, j) == 3:
                newboard[j]='x'


    x.write(''.join(newboard))
    x.write('\n')


board=[]
x = open('res', 'w')
f=open('theboard','r')

line1=f.readline().split()
n=len(line1)
board.append(['0']*n)
board.append(line1)
board.append(f.readline().split())
f.close()

gameOfLife2(board)
board=[]
with open('theboard','r') as file:
    for line in file:
        if line:
            board.append(line.split())

            if len(board)==3:
                gameOfLife2(board)
                board.remove(board[0])

board.append(n*['0'])
gameOfLife2(board)


# board = [['x', 'x'], ['x', '0']]
# board = [['x']]
# board = [['x',0]]

#gameOfLife1(board)
#print board
