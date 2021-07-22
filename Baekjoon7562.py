from collections import deque

testcase = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
for _ in range(testcase):
    l = int(input())
    x, y = map(int, input().rstrip().split())
    goalx, goaly = map(int, input().rstrip().split())
    visit = [[-1] * l for _ in range(l)]

    queue = deque()
    queue.append((x, y))
    visit[x][y] = 0
    check = True

    while queue:
        curx, cury = queue.popleft()
        if curx == goalx and cury == goaly:
            print(visit[curx][cury])
        for i in range(8):
            newx = curx + dx[i]
            newy = cury + dy[i]
            if 0 <= newx < l and 0 <= newy < l and visit[newx][newy] == -1:
                if newx == goalx and newy == goaly:
                    print(visit[curx][cury] + 1)
                    check = False
                    break
                else:
                    queue.append((newx, newy))
                    visit[newx][newy] = visit[curx][cury] + 1
        if not check:
            break
