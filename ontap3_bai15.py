# Bài 15: Viết chương trình Python chuyển các phần tử dương của danh sách lên đầu danh sách và in danh sách ra màn hình.
item1=[1,10,-7,6,-3,4,5,2,-1] 
item2=[10,7,-3,4,3,2,1]  
item3=[10,7,4,3,2,1]  
item4=[-10,-7,-3,-4,-3,-2,-1]  

def arrg(item): #5n+1 -> O(n)=n
    left=0
    right=len(item)-1 
    while left < right: #n+1 
        if item[left]<0 and item[right]>0:#2n
            item[left],item[right]=item[right],item[left]
        if item[left]>0: #n
            left+=1
        if item[right]<0: #n
            right-=1
    return item 

print(arrg(item1))
print(arrg(item2))
print(arrg(item3))
print(arrg(item4))

                    