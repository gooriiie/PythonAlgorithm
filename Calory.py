import sys

N, K = map(float, sys.stdin.readline().split(" "))
N, K = int(N), int(K * 100)

dp = [0 for _ in range(K+1)]

for _ in range(N):
    price, calory = map(float, sys.stdin.readline().split(" "))
    price, calory = int(price * 100), int(calory)

    for i in range(price, K+1):
        dp[i] = max(dp[i], dp[i-price] + calory)

print(dp[K])
