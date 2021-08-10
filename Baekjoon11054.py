import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
dp = [1] * N
dp2 = [1] * N
result = [0] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(N):
    result[i] = dp[i] + dp2[i]

print(max(result) - 1)
