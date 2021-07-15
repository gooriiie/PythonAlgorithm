
N, C = map(int, input().rstrip().split())

home = []

for _ in range(N):
    home.append(int(input()))

home.sort()

left = 1
right = max(home) - min(home)
result = []

while left <= right:
    mid = (left + right) // 2

    check = min(home)
    count = 1

    for i in range(1, len(home)):
        if home[i] >= check + mid:
            count += 1
            check = home[i]

    if count < C:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)