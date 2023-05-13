item1 = [500, 430, 12, 430, 55, 430,500]

def findMax(arr): #4n-4 -> O(n)=n
    p=0
    for i in range (1,len(arr)): #n
        if arr[i] > arr[p]: #n-1
            p=i 
    arr[p],arr[0] = arr[0],arr[p] 
    p=1
    for i in range (2,len(arr)): #n-1
        if arr[i] > arr[p]: #n-2
            p=i 
    return arr[p]
            
print(findMax(item1))