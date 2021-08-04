import sys

N, M = map(int, sys.stdin.readline().split())
gods = []
already = []
edges = []
parent = list(range(N))


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    gods.append((x, y))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    god1 = gods[a-1]
    god2 = gods[b-1]
    weight = ((god1[0]-god2[0]) ** 2 + (god1[1]-god2[1]) ** 2) ** 0.5
    already.append((weight, a-1, b-1))

for i in range(N):
    for j in range(i+1, N):
        if i == j:
            continue
        else:
            god1 = gods[i]
            god2 = gods[j]
            weight = ((god1[0]-god2[0]) ** 2 + (god1[1]-god2[1]) ** 2) ** 0.5
            edges.append((weight, i, j))

for edge in already:
    weight, god1, god2 = edge
    if find(god1) == find(god2):
        continue
    else:
        union(god1, god2)

edges.sort()
cost = 0
for edge in edges:
    weight, god1, god2 = edge
    if find(god1) == find(god2):
        continue
    else:
        union(god1, god2)
        cost += weight

print("%0.2f" % cost)
