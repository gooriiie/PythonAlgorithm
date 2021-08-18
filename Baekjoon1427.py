import sys

N = sys.stdin.readline().rstrip()
N = list(map(int, N))
N.sort(reverse=True)
for i in N:
    print(i, end="")
