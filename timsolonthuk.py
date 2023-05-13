# def findMax(arr): #4n-4 -> O(n)=n
#     p=0
#     for i in range (1,len(arr)): #n
#         if arr[i] > arr[p]: #n-1
#             p=i 
#     arr[p],arr[0] = arr[0],arr[p] 
#     p=1
#     for i in range (2,len(arr)): #n-1
#         if arr[i] > arr[p]: #n-2
#             p=i 
#     return arr[p]
item1=[1,2,4,6,8,9,12,13,3,0,7]
def findMax(arr,k):
    arr=arr.copy()
    for j in range(k):
        p=j
        for i in range (p+1,len(arr)):
            if arr[i] > arr[p]:
                p=i
        arr[p],arr[j]=arr[j],arr[p] 
    return arr[j]

print(findMax(item1,3))    
print(findMax(item1,4))    
print(item1)