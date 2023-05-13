s1='abcba'
s2='abcbaf'

def isSymetric(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False 
    return True

print(isSymetric(s1))
print(isSymetric(s2))
