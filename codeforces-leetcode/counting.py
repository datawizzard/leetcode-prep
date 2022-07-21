import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def sumofdig(n):
	a=[]
	s="11"
	for i in range(3,n+1):
		count=1
		lol=""
		s+='@'
		for j in range(1,len(s)):
			if s[j]!=s[j-1]:
				lol+=str(count)
				lol+=s[j-1]
				count=1
			else:
				count+=1
		s=lol
		print(s)
		sum1=0
		for i in s:
			sum1+=int(i)
		a.append(sum1)
	return a
N=int(input())
arr=list(map(int,input().split()))
k=sumofdig(N)
# m=getsum(k)
a=[1,2]
a.extend(k)
for i in arr:
	print(a[i-1])


