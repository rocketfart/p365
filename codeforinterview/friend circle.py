# Enter your code here. Read input from STDIN. Print output to STDOUT

def find(n, matrix):

    def dfs(x):
        visited.append(x)
        for i in range(n):
            if i != x and i not in visited and matrix[x][i] == 'Y':
                dfs(i)

    visited = []
    count = 0

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1
    print count
    return


matrix = []
n = int(raw_input())
while True:
    try:
        line = raw_input()
        numbers = [i for i in list(line)]
        matrix.append(numbers)
    except:
        find(n, matrix)
        break

