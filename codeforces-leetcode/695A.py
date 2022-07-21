import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def isvalley(i):
	return (i>0 and i<n-1 and a[i-1] > a[i] < a[i + 1])
def ishill(i):
	return (i>0 and i<n-1 and a[i-1] < a[i] > a[i + 1])
def findLocalMaximaMinima(n, a):
	ans=s  
	for i in range(1,n-1):  
		temp=a[i]   
		a[i] = a[i - 1]
		ans = min(ans, s - vis[i - 1] - vis[i] - vis[i + 1] + ishill(i-1) + ishill(i) + ishill(i+1) + isvalley(i-1) + isvalley(i) + isvalley(i+1))
		a[i] = a[i + 1]
		ans = min(ans, s - vis[i - 1] - vis[i] - vis[i + 1] + ishill(i-1) + ishill(i) + ishill(i+1) + isvalley(i-1) + isvalley(i) + isvalley(i+1))
		a[i] = temp
	return ans
for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	vis=[0]*n
	s = 0
	for i in range(1,n-1):
	    if (ishill(i) or isvalley(i)):
	        vis[i] = 1
	        s+=1
	# print(vis,s)        
	print(findLocalMaximaMinima(n,a))




