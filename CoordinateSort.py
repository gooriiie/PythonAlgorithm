import sys
from bisect import bisect_left, bisect_right

N = int(input())

coordinate = list(map(int, sys.stdin.readline().rstrip().split()))

# 2 4 -10 4 -9
# 1000 999 1000 999 1000 999

sortedCoordinate = sorted(list(set(coordinate)))

# -10 -9 2 4 4
# 999 999 999 1000 1000 1000
# 999 1000

for i in range(N):
    index = bisect_left(sortedCoordinate, coordinate[i])
    print(index, end=" ")