import heapq
import sys

V, E = map(int, sys.stdin.readline().rstrip().split())
K = int(input())
graph = [[] for _ in range(V+1)]
INF = 1e9
distance = [INF] * (V+1)

for _ in range(E):
    start, end, weight = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append([weight, end])

queue = []
heapq.heappush(queue, (0, K))
distance[K] = 0
while queue:
    w, cur = heapq.heappop(queue)
    if w > distance[cur]:
        continue
    for weight, end in graph[cur]:
        if w + weight < distance[end]:
            distance[end] = w + weight
            heapq.heappush(queue, (weight + w, end))

for i in range(1, V+1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print("INF")