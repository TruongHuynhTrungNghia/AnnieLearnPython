def f(x):
    return x**3+x**2+x-1 
def solve(a,b):
    c = (a+b)/2
    e = 0.0001
    while abs(f(c))>=e:
        if f(a)*f(c) > 0:
            a = c 
        else:
            b = c
        
        c = (a+b)/2
    return c 

print(solve(0,1))        