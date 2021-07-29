
n = int(input())
dp = []
#  dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
for i in range(n):
    dp.append(list(map(int, input().split())))

col = 2
for i in range(1, n):
    for j in range(col):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        elif j == col-1:
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
    col += 1
print(max(dp[n-1]))

