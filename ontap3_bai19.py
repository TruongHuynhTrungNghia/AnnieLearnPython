# Bài 19: Tìm tần suất xuất hiện của một ký tự trong một chuỗi.
S = 'hellokitty'
def count(s,ch): #2n+1 -> O(n)=n
    c = 0
    for v in s: #n+1
         if v==ch: #n
             c+=1
    return c 

print(count(S,'l'))
