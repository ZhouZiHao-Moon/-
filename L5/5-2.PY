L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def func1(n):
    return n[0]
def func2(n):
    return n[1]
print(sorted(L,key=func1))
print(sorted(L,key=func2,reverse=True))
