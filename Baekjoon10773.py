
K = int(input())
arr = []
result = 0

for _ in range(K):
    number = int(input())
    if number != 0:
        arr.append(number)
    else:
        arr.pop()

for i in range(len(arr)):
    result += arr[i]

print(result)