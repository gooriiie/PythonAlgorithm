import sys

N = int(input())
result = N
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            result -= 1
            break
print(result)
