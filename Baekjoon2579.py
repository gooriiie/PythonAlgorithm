
floor = int(input())
dp = [0] * (floor+1)
stair = [0] * (floor+1)

for i in range(1, floor+1):
    stair[i] = int(input())

for i in range(1, floor+1):
    if i == 1:
        dp[i] = stair[i]
    elif i == 2:
        dp[i] = max(dp[i-1] + stair[i], stair[i])
    else:
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[floor])