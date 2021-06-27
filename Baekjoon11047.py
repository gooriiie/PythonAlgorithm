import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coin = list()
result = 0

for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in range(N):
    result += K // coin[i]
    K = K % coin[i]

print(result)