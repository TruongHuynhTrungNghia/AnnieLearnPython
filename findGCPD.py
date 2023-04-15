def greatestCommonPrimeDivisor(a,b):
    while abs(a-b)>0:
        if a>b:
            a=a-b
        if b>a:
            b=b-a
    else:
        return a   

print(greatestCommonPrimeDivisor(12, 18))
