S1='AAA'
T1='ABC'

S2='ABC'
T2='CAB'

def check(S,T):
    arrS=[0]*26
    arrT=[0]*26 
    for i in range(len(S)):
        arrS[ord(S[i])-ord('A')] +=1
        arrT[ord(T[i])-ord('A')] +=1
    return arrS == arrT 

print(check(S1,T1))
print(check(S2,T2))