import sys
'''
4 4
R R R R
L L L L
R R R R
L L L L
'''

M, N = map(int, sys.stdin.readline().rstrip().split(" "))
direction = [[""] * N for _ in range(M)]

for i in range(M):
    tmp = list(sys.stdin.readline().rstrip().split(" "))
    for j in range(N):
        direction[i][j] = tmp[j]

for i in range(M):
    for j in range(N):
        print(direction[i][j], end="")
    print()


