import sys

sentence1 = sys.stdin.readline().rstrip()
sentence2 = sys.stdin.readline().rstrip()

dp = [[0] * (len(sentence1)+1) for _ in range(len(sentence2)+1)]
for i in range(1, len(sentence2) + 1):
    for j in range(1, len(sentence1) + 1):
        if sentence1[j-1] == sentence2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(max(dp[len(sentence2)]))
