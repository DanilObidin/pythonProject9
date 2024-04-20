for a in range(1, 9+1):
    for a in range(0, 9+1):
        ab = (a*10+b)
        cab = (a*10+b)*(a*10+b)
        if cab > 99 and cab < 1000 and cab%100 == ab:
            print(cab)
        
