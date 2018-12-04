def ritka(n):
    if n <= 2:
        return n-1
    f0 = 1
    f1 = 2
    p = 1
    while f1 < n:
        tmp = f0
        f0 = f1
        f1 += tmp
        p <<= 1 # binaris jobbra tolás 1-gyel, azaz szorzás 2-vel
    return p + ritka(n-f0)

print(ritka(int(input())))
