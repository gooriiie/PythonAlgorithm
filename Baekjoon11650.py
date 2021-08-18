import sys

N = int(input())
point = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    point.append((x, y))

point.sort()
for p in point:
    x, y = p
    print(x, y)
