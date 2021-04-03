import sys
from itertools import permutations

number = sys.stdin.readline().rstrip()

prime_number = []

for i in range(len(number)):
    per = list(permutations(number, i+1))
    for j in range(len(per)):
        int_change = (int)("".join(per[j]))
        count = 0
        for k in range(2,int_change+1):
            if int_change % k == 0:
                count += 1
            else:
                continue
        if count == 1:
            prime_number.append(int_change)

prime_number_set = set(prime_number)
print(len(prime_number_set))



