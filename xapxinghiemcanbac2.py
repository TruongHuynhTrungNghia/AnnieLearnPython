def sqr(n):
    a=0
    b=n
    x = (a+b)/2
    e=0.0001
    while abs(x*x -n) > e:
        if x*x > n:
            b = x
        else:
            a = x 
        x = (a+b)/2 
    return x  

n = 10
print(sqr(n))