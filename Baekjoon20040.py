import sys

n, m = map(int, sys.stdin.readline().split())
parent = list(range(n))


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


check = True
for i in range(m):
    point1, point2 = map(int, sys.stdin.readline().split())
    if find(point1) == find(point2):
        check = False
        print(i+1)
        break
    else:
        union(point1, point2)
        continue

if check:
    print(0)
