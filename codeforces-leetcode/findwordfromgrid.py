import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
class Solution:
	def d(self,a,b,n,i,r,c):
		#print("start")
		if i>=len(b) or r<0 or c<0 or r>=n or c>=n or a[r][c]!=b[i]:
			return False
		else:
			a[r][c]="$"
			print(a[r][c],b[i],r,c)
			retval=False
			row=[-1,1,0,0]
			col=[0,0,-1,1]
			for d in range(0,4):
				s=r+row[d]
				t=c+col[d]
				retval=self.d(a,b,n,i+1,s,t)
				print(retval,"gy",d,i,s,t)	
			a[r][c]=b[i]
			if i==len()
			print(a[r][c],r,c,"ff",i)
			return retval
	def numofislands(self,a,b):
		for i in range(len(a)):
			for j in range(len(a[0])):
				if a[i][j]==b[0]:
					#print(a[i][j],b[0],i,j)
					if self.d(a,b,n,0,i,j)==True:
						return True
		return False
n=int(input())
a =[list(input().split()) for i in range(n)]
b=input()
#print(a)
x=Solution()
print(x.numofislands(a,b))