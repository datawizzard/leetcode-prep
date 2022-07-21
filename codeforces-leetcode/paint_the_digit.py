# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
for _ in range(int(input())):
	n = int(input())
	ar = list(map(int,input()))
	# d = ar[:]
	# d.sort()
	# c_arr = [2]*n
	# x = 0
	# # print(ar)
	# # print(d)   
	# for i in range(n):
	#     if ar[i] == d[x]:            
	#         c_arr[i] = 1
	#         x += 1
	# # print(c_arr)
	# chk_arr = []
	# for i in range(n): 
	# 	if c_arr[i] == 1:
	# 		chk_arr.append(ar[i])
	# # print(chk_arr)
	# for i in range(n):
	#     if c_arr[i] == 2:
	#         chk_arr.append(ar[i])
	# # print(chk_arr)
	# if chk_arr == d:
	#     for i in range(n):
	#         print(c_arr[i],end= '')
	#     print()
	# else:
	#     print('-')
	ss = ar[:]
	ans = ar
	ss.sort()
	idx = 0
	# print(ar)
	# print(ss)
	for i in range(n):
		if(ar[i]==ss[idx]):
			ar[i]=1
			ans[i]='1'
			idx += 1
	for i in range(n):
		if(idx<=n-1 and ar[i]==ss[idx]):
			ar[i]=1
			ans[i]='2'
			idx += 1
			# print(idx)
			# print(ar)			
			# print(ans)
	if idx != n:
		ans = "-"
	print(*ans,sep="")