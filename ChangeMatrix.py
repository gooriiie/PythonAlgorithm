import sys
import heapq
'''
4 3
20 -21 14
-19 4 19
22 -47 24
-19 4 19
'''
M, N = map(int, sys.stdin.readline().rstrip().split(" "))
matrix = [[0] * N for _ in range(M)]
result = [[1] * N for _ in range(M)]
heap = []

for i in range(M):
    tmp = list(sys.stdin.readline().rstrip().split(" "))
    for j in range(N):
        matrix[i][j] = (int)(tmp[j])
        heapq.heappush(heap, (matrix[i][j], (i, j)))

while heap:
    value, (i, j) = heapq.heappop(heap)

    for k in range(M):
        if k != i:
            if value < matrix[k][j]:
                result[k][j] = max(result[i][j] + 1, result[k][j])
            else:
                continue

    for k in range(N):
        if k != j:
            if value < matrix[i][k]:
                result[i][k] = max(result[i][j] + 1, result[i][k])
            else:
                continue

for i in range(M):
    for j in range(N):
        print(result[i][j], end=" ")
    print()



