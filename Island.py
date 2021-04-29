import sys
from collections import deque

N = (int)(input())
count = 0
result = sys.maxsize

visited = [[False] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x,y):
    if arr[x][y] == 1:
        if visited[x][y] == False:
            visited[x][y] = True
            arr[x][y] = count + 1
        else:
            return
    else:
        return

    for k in range(4):
        newX = x + dx[k]
        newY = y + dy[k]
        if newX >= 0 and newX < N and newY >= 0 and newY < N:
            dfs(newX, newY)

    return True

def bfs(n):
    queue = deque()
    distance = [[0] * N for _ in range(N)]
    visited1 = [[False] * N for _ in range(N)]
    global result

    for i in range(N):
        for j in range(N):
            if arr[i][j] == n:
                queue.append([i, j])
                visited1[i][j] = True

    while queue:
        tmp = queue.popleft()

        for k in range(4):
            newX = tmp[0] + dx[k]
            newY = tmp[1] + dy[k]

            if newX >= 0 and newX < N and newY >= 0 and newY < N and visited1[newX][newY] == False:
                if arr[newX][newY] != 0 and arr[newX][newY] == n:
                    queue.append([newX, newY])
                    visited1[newX][newY] = True

                elif arr[newX][newY] == 0 and arr[newX][newY] != n:
                    queue.append([newX, newY])
                    distance[newX][newY] = distance[tmp[0]][tmp[1]] + 1
                    visited1[newX][newY] = True

                elif arr[newX][newY] != 0 and arr[newX][newY] != n:
                    result = min(result, distance[tmp[0]][tmp[1]])
                    return


arr = [[0] * N for _ in range(N)]

for i in range(N):
    data = sys.stdin.readline().rstrip().split(" ")
    for j in range(N):
        arr[i][j] = (int)(data[j])

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            count += 1

for i in range(2, count+1):
    bfs(i)

print(result)