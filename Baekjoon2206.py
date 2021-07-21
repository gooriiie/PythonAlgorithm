import sys
from collections import deque

N, M = map(int, input().split())
arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
queue = deque()
queue.append((0, 0, 0))
visit[0][0][0] = 1

check = False
while queue:
    x, y, state = queue.popleft()
    if x == N-1 and y == M-1:
        print(visit[x][y][state])
        check = True
        break
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < N and 0 <= newy < M and visit[newx][newy][state] == 0:
            if int(arr[newx][newy]) == 0:
                visit[newx][newy][state] = visit[x][y][state] + 1
                queue.append((newx, newy, state))
            if int(arr[newx][newy]) == 1 and state == 0:
                visit[newx][newy][1] = visit[x][y][state] + 1
                queue.append((newx, newy, 1))

if not check:
    print(-1)
