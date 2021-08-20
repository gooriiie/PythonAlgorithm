import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
arr = list(range(1, N+1))
nPr = list(permutations(arr, M))
nPr.sort()

for i in nPr:
    for j in i:
        print(j, end=" ")
    print()
