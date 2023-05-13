S='abc'
S1='abcdef'

def reverse(s):
    arr=[0]*len(s)
    for i in range(len(s)):
        arr[i]=s[len(s)-i-1]
    return ''.join(arr)
    
print(reverse(S))
print(reverse(S1))