import sys
import heapq

N, E = map(int, sys.stdin.readline().rstrip().split())
INF = 1e9
graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, sys.stdin.readline().rstrip().split())


def dijkstra(start, goal):
    distance = [INF] * (N + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        w, cur = heapq.heappop(queue)
        if w > distance[cur]:
            continue
        for weight, end in graph[cur]:
            if w + weight < distance[end]:
                distance[end] = w + weight
                heapq.heappush(queue, (weight + w, end))
    return distance[goal]


case1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
case2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
if min(case1, case2) < INF:
    print(min(case1, case2))
else:
    print(-1)