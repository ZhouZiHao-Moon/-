import math

l=([1,2,1],[9,-15,-6],[1,1,4])

def func(*num):
    a=num[0]
    b=num[1]
    c=num[2]
    t=b*b-4*a*c
    if t<0:
        return "no real roots"
    else:
        x1=(-1*b+math.sqrt(t))/(2*a)
        x2=(-1*b-math.sqrt(t))/(2*a)
        return x1,x2

for ll in l:
    print(func(*ll))
        
