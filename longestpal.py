import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
s=input()
#brute_force
# n=len(s)
# best_sub=""
# best_len=0
# for L in range(n):
# 	for R in range(L,n+1):
# 		sub=s[L:R+1]
# 		t=R-L+1
# 		if  t>best_len and sub==sub[::-1]:
# 			best_len=t
# 			best_sub=sub
# print(best_sub)
#Logic:
# For string of odd length we take a middle element of any substring
# and check whether i-1 and i+1 till are equal they are not 
# different and store the substring and length of that substring.
# For string of even length we take a middle element of length two 
# and check whether i-1 and i+1+1 are qual till they are not different
# and store the lenth of substring and length of that substring.
def helper(s,l,r):
    while (l >=0 and r < len(s) and s[l] == s[r]):
        l-=1
        r+=1
    return s[l+1:r]
# s="babad"
result=""    
for i in range(len(s)):
    test=helper(s,i,i+1)
    if len(test) > len(result): 
        result=test
    test=helper(s,i,i)
    if len(test) > len(result): 
        result=test
print(result)
