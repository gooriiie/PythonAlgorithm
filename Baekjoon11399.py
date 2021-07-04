import sys

N = int(input())

time = list(map(int, sys.stdin.readline().rstrip().split()))

time.sort()

wait = 0

for i in range(N):
    current = time[i]
    for j in range(i, N):
       wait += current

print(wait)