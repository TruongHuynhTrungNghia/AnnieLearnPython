S='xinchaoban'
s='chao'
s1='hcao'
def checkEqual(S,s,i):
    for j in range(len(s)):
        if s[j] != S[i+j]:
            return False
    return True

def isSubString(S,s):
    for i in range(len(S)-len(s)+1):
        if checkEqual(S,s,i):
            return True 
    return False

print(isSubString(S,s))
print(isSubString(S,s1))
                 