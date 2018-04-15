def yangHuiTriangle():
    L=[1]
    while True:
        yield L
        L = [1]+[L[i-1] + L[i] for i in range(1,len(L))]+[1]
n=0
for t in yangHuiTriangle():
    print(t)
    n=n+1
    if n==10:        
        break
