import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
# for _ in range(II()):
# 	n,k =MI()
# 	arr = LI()
# 	for i in range(n):
# 		if arr[i] % k == 0:
# 			continue
# 		else:
# 			if arr[i]*2 % k != 0:
# 				print("NO")
# 				break;
# 	else:
# 		print("YES")
# for _ in range(II()):
# 	n = II()
# 	a = I()
# 	c = 0
# 	l = a.count("10")
# 	while l!=0:
# 		a = a.replace('10','',1)
# 		c += 1
# 		l = a.count("10")
# 	print(c)
# def solve():
# 	e,o,res,temp = 0,0,0,0
# 	if a[0] == '0':
# 		e = 1
# 	else:
# 		o = 1
# 	for i in range(1,n):
# 		res = 0
# 		if a[i] == '1':
# 			res = max(e,o)
# 			res += 1
# 			o = res
# 		else:
# 			res = max(e,0)
# 			res += 1
# 			e = res
# 	temp = max(e,o)
# 	return temp
# for _ in range(II()):
# 	n = II()
# 	a = I()
# 	print(n-solve())
# def lis(arr): 
#     n = len(arr) 
 
#     lis = [1]*n 
#     for i in range (1 , n): 
#         for j in range(0 , i): 
#             if arr[i] >= arr[j] and lis[i]< lis[j] + 1 : 
#                 lis[i] = lis[j]+1 
#     maximum = 0 
#     for i in range(n): 
#         maximum = max(maximum , lis[i])   
#     return maximum 
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    ans = 0
    if s==sorted(s):
        ans = 0
    else:
        c = 0
        for i in range(n):
            if s[i]=='1':
                c+=1
            else:
                if c>0:
                    c-=1
                    ans+=1
    print(ans)
	

