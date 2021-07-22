
T = int(input())

for _ in range(T):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    N = int(input())
    if N >= 3:
        for i in range(3, N+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[N], one[N])

