## Bài 10: Viết chương trình Python tính số lượng các phần tử liên tiếp đan dấu nhiều nhất (dãy phần tử liên tiếp được gọi là đan dấu nếu tích hai phần tử liên tiếp âm).

item1=[1,-1,2,-3,-4,5,-6,4,-2]
item2=[1,-1,2,-3,4,-6,4,4,-2,1]
item3=[0,-1,1,1,1,1,1,1]

def find(item): #3n-1 -> O(n) = n 
    countmax=0
    count=1
    for i in range(1,len(item)): #n
        if item[i-1]*item[i] <0:# them or de xu ly th bang 0
            count +=1
        else:
            if count>countmax: #2n-2 
                countmax=count
            count = 1 
    if count>countmax: #1
        countmax=count
    return countmax

print(find(item3))                