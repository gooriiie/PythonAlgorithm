import sys

N = int(input())
M = int(input())
city = []
parent = list(range(N))
for _ in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))

plan = list(map(int, sys.stdin.readline().split()))


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


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if city[i][j] == 1:
            if find(i) == find(j):
                continue
            else:
                union(i, j)

result = set([find(i-1) for i in plan])
if len(result) == 1:
    print("YES")
else:
    print("NO")
