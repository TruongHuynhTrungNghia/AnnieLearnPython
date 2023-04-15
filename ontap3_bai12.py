# Bài 12: Viết chương trình Python tìm vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất.
item1=[1,10,-7,6,-3,4,5,2,-1] 
item2=[10,7,-3,4,3,2,1] 
item3=[10,-3,4,-3,2,1,1,8,7,6,5,4,3,2,-1] 
def findConsequence(item): #3n+2 ->O(n)=n  
    indexmax=None
    count=0
    countmax=0
    for i in range(len(item)): #n+1
        if item[i]>0:
            count+=1
        else:
            if count>countmax:#2n
                countmax=count
                indexmax=i-countmax
            count=0        
    if count>countmax: #1
        indexmax=len(item)-count
    return indexmax
print(findConsequence(item1))                
print(findConsequence(item2))                
print(findConsequence(item3))                
                
        
    
