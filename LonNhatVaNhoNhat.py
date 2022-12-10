while(1):
    n = int(input())
    if n ==0: break
    else:
        a = []
        for i in range(n):
            x = input()
            a.append(int(x))
        ma = max(a)
        mi = min(a)
        if(ma == mi): print("BANG NHAU")
        else: print("{} {}".format(mi,ma))