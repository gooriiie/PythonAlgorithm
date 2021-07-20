from collections import deque

N, K = map(int, input().split())

visit = [0] * 100001
queue = deque([])
queue.append(N)

while queue:
    point = queue.popleft()
    if point == K:
        print(visit[point])
        break
    for newx in (point-1, point+1, 2*point):
        if 0 <= newx <= 100000 and visit[newx] == 0:
            visit[newx] = visit[point] + 1
            queue.append(newx)

