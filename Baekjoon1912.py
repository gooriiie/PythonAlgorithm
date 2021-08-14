import sys

n = int(input())
number = list(map(int, sys.stdin.readline().split()))
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = number[i]
    dp[i] = max(dp[i-1] + number[i], number[i])

print(max(dp))
