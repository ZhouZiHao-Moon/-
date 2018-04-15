def off(x):
    return x%n!=0
l=range(2,1001)
n=0
def prime():
    global l,n
    while True:
        n=l[0]
        yield n
        l=list(filter(off,l))
for i in prime():
    if i<1000:
        print(i)
    else:
        break
