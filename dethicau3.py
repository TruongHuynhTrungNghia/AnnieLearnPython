#tim kiem tuyen tinh
L=[9,7,4,3,2] 

def search(x,arr): #O(n)
    n=len(arr)
    for v in arr:
        if v == x:
            return True 
    return False 
#print(search(9,L))
#print(search(1,L))
#print(search(0,L))

#tim kiem nhi phan 

def searchBinary(x,l): # O(log2(n))
    left=0
    right=len(l)-1
    while left < right:
        mid = (left+right)//2
        if x==l[mid]:
            return True 
        if x > l[mid]:
            right=mid-1 
        else:
            left=mid+1
    return False 
    
print(searchBinary(9,L))
print(searchBinary(1,L))
print(searchBinary(0,L))