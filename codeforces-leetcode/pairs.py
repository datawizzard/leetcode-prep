import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# for _ in range(int(input())):
#     n = int(input())
#     b = list(map(int, input().split()))
#     maxi,mini,t,pos=0,0,0,0
#     for i in range(0,n):
#         t-=b[i]-pos-1;
#         mini=min(mini,t);
#         # print(t,mini)
#         t+=1
#         maxi=max(maxi,t);
#         pos=b[i];
#         # print(pos,maxi)
#     print(n-maxi+mini+1)
# for z in range(int(input())):
# 	n = int(input())
# 	a = [1]*(2*n)
# 	for i in map(int, input().split()):
# 		a[i-1] = -1
# 	# print(*a)
# 	x = 0
# 	s = 0
# 	for i in a:
# 		if i < 0:
# 			if s > 0:
# 				x += 1
# 				s -= 1
# 				# print(x,s)
# 		else:
# 			s += 1
# 	# print(x)
	
# 	y = 0
# 	s = 0
# 	for j in range(2*n-1, -1, -1):
# 		if a[j] < 0:
# 			if s > 0:
# 				y += 1
# 				s -= 1
# 				# print(y,s)
# 		else:
# 			s += 1
# 	# print(y,"ff")
# 	x = n - x
# 	if x < y:
# 		x, y = y, x

# 	# print(x,y)
# 	print(x - y + 1)
def binary(a,c,n):
	ans,low,high=0,0,n-1
	while low<=high:
		k=(low+high)//2
		flag=1
		for i in range(k+1):
			if a[i]>c[n-1-k+i]:
				flag=0
		if flag:
			ans=k+1
			low=k+1
		else:
			high=k-1
	return ans
for _ in range(int(input())):
	n=int(input())
	b=list(map(int,input().split()))
	H=[0]*(2*n)
	# print(H)
	for i in b:
		H[i-1]=1
	# print(H)
	a=[]
	c=[]
	for i in range(2*n):
		if H[i]==0:
			a.append(i+1)
		else:
			c.append(i+1)
	print(*a)
	print(*c)
	n1=binary(a,c,n)
	print(n1)
	n2=n-binary(c,a,n)
	print(n2)
	print(max(0,n1-n2+1))

