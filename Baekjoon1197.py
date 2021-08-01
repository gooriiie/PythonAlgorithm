import sys

V, E = map(int, sys.stdin.readline().split())
edges = []
parent = list(range(V+1))
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((C, A, B))

edges.sort()


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


cost = 0
for edge in edges:
    weight, a, b = edge
    if find(a) == find(b):
        continue
    else:
        union(a, b)
        cost += weight

print(cost)
