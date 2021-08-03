import sys

n = int(input())
edges = []
stars = []
parent = list(range(n+1))


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


for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

for i in range(n):
    for j in range(i+1, n):
        if i == j:
            continue
        else:
            star1 = stars[i]
            star2 = stars[j]
            weight = round(((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5, 2)
            edges.append((weight, star1, star2, i, j))
edges.sort()
cost = 0
for edge in edges:
    weight, star1, star2, number1, number2 = edge
    if find(number1) == find(number2):
        continue
    else:
        union(number1, number2)
        cost += weight
print(cost)
