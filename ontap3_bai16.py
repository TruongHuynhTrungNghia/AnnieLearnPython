# Bài 16: Viết chương trình Python tìm
# số phần tử là dương
# và là số nguyên tố của danh sách 
# và vị trí của nó trong danh sách. 
item3=[10,7,4,3,2,1]  

def is_prime(n):#2(n**0.5)-2
    if n<2: #1
        return False 
    for i in range(2,int(n**0.5)+1): #n**0.5-1
        if n%i==0: #n**0.5-2
            return False 
    return True 

def find(item): #2n*(n**0.5) -3n + 1 -> O(n*(n**0.5))=n*(n**0.5)
    a=[]
    for i in range(len(item)): #n+1
        if is_prime(item[i])==True: # n*(2(n**0.5)-2) =2n*(n**0.5) - 4n
            a.append(i)
    return a

print(find(item3))
