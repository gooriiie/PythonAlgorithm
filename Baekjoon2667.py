import sys

N = int(input())

home = [sys.stdin.readline().rstrip() for i in range(N)]
check = [[False] * N for _ in range(N)]
count = 0
totalCount = 0
countList = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(a, b):
    global count
    if not check[a][b] and int(home[a][b]) == 1:
        check[a][b] = True
        count += 1
        for k in range(4):
            newx = a + dx[k]
            newy = b + dy[k]
            if 0 <= newx < N and 0 <= newy < N:
                dfs(newx, newy)
    return


for i in range(N):
    for j in range(N):
        if int(home[i][j]) == 1 and not check[i][j]:
            totalCount += 1
            dfs(i, j)
            countList.append(count)
            count = 0

countList.sort()
print(totalCount)
for i in countList:
    print(i)
