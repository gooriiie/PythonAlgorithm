import sys

word = sys.stdin.readline().rstrip()
count = 0

while word:
    if "c=" in word:
        word = word.replace("c=", "*", 1)
    elif "c-" in word:
        word = word.replace("c-", "*", 1)
    elif "dz=" in word:
        word = word.replace("dz=", "*", 1)
    elif "d-" in word:
        word = word.replace("d-", "*", 1)
    elif "lj" in word:
        word = word.replace("lj", "*", 1)
    elif "nj" in word:
        word = word.replace("nj", "*", 1)
    elif "s=" in word:
        word = word.replace("s=", "*", 1)
    elif "z=" in word:
        word = word.replace("z=", "*", 1)
    else:
        count = len(word)
        word = ""

print(count)
