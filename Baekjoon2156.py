
n = int(input())

dp = [0] * (n+1)
arr = [0] * (n+1)

for i in range(1, n+1):
    arr[i] = int(input())
    if i == 1:
        dp[i] = arr[i]
    elif i == 2:
        dp[i] = dp[i-1] + arr[i]
    else:
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i], dp[i-1])

print(dp[n])