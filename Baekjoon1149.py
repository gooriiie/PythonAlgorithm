import sys

N = int(input())
dp = [[0] * 3 for _ in range(1001)]
for i in range(1, N+1):
    red, green, blue = map(int, sys.stdin.readline().split())
    if i == 1:
        dp[i][0] = red
        dp[i][1] = green
        dp[i][2] = blue
    else:
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + red
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + green
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + blue

print(min(dp[N]))
