k = 0
for i in range(1, 999999):
    if i % 10 == i // 100000 and i // 10 % 10 == i // 10000 % 10 and i // 100 % 10 == i // 1000 % 10 and i > 100000:
        k = i
        break
print(k)
