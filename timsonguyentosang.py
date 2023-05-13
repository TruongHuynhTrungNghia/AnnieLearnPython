n =int(input('Nhap n'))
arr = list(range(n))
arr[0]=arr[1]=0
for i in range (2,n//2+1):
    if arr[i] != 0:
        for j in range(i*2,n,i):
            arr[j]=0
for v in arr:
    if v !=0:
        print(v)