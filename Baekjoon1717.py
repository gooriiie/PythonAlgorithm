import sys
sys.setrecursionlimit(1000000)

n, m = map(int, sys.stdin.readline().split())
parent = list(range(n+1))


def find(i):
    if i == parent[i]:
        return i
    parent[i] = find(parent[i])
    return parent[i]


def union(i, j):
    i = find(i)
    j = find(j)
    if i < j:
        parent[j] = i
    else:
        parent[i] = j


for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:
        if find(a) == find(b):
            continue
        else:
            union(a, b)
    elif op == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
