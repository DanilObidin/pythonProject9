for i in range(1, 9+1):
    for j in range(0, 9+1):
        c = (i*10+j) * (i*10+j)
        if c%1000 == i*100+j and c < 1000:
            print(c)
