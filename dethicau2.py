L=[7,4,5,3,1]

def sort(arr):
    n = len(arr) 
    for i in range(n-1):
        pmin=i
        for j in range(i+1,n):
            if arr[pmin]>arr[j]:
                pmin=j
        arr[pmin], arr[i] = arr[i],arr[pmin]   
    
sort(L)
print(L)