n = int(input())
k = 0
c = []
for i in range(2, n):
    if n % i == 0:
        k = i
        c.append(k)
print(min(c))
