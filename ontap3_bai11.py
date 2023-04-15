# Bài 11: Viết chương trình Python tính số lượng các phần tử không tăng nhiều nhất.
item1=[1,10,7,6,3,4,5,2,1] 
item2=[10,7,3,4,3,2,1]
def findConsequence(item): #3n-1 ->O(n)=n
    count=1
    countmax=0 
    for i in range(1,len(item)): #n
        if item[i-1]>item[i]:
            count+=1
        else:
            if count>countmax: #2n-2
                countmax=count
            count=1
    if count>countmax: #1
        countmax=count 
    return countmax 

print(findConsequence(item1))                
print(findConsequence(item2))                
