from functools import reduce

def prod(x,y):
    return x*y

print('3 * 5 * 7 * 9 =', reduce(prod,[3, 5, 7, 9]))
