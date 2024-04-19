k = 0
f = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        k += n
        if k / 4 > n:
            f += 1
print(f)