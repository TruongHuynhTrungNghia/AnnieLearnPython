# Bài 20: Đảo ngược chuỗi.
S = 'hellokitty'
def reverse(s): #n*0.5+1 
    s=list(s)
    left=0
    right=len(s)-1 
    while left < right: #n*0.5+1
        s[left],s[right]=s[right],s[left]
        left+=1
        right+-1
    return ''.join(s) 

print(reverse(S))     
    