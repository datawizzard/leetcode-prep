import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
class Solution:
	def numofislands(self,a):
		c=0
		for i in range(len(a)):
			for j in range(len(a[0])):
				if a[i][j]==1:
					self.d(a,i,j)
					#print("hhd")
					c+=1
		return c
	def d(self,a,i,j):
		#print("start")
		if 0<=i and 0<=j and i<len(a) and j<len(a[0]) and a[i][j]==1:
			a[i][j]="#"
			self.d(a,i+1,j)
			self.d(a,i-1,j)
			self.d(a,i,j+1)
			self.d(a,i,j-1)
		return
n,m=map(int,input().split())
a =[list(map(int, input().split())) for i in range(n)]
#print(a)
x=Solution()
print(x.numofislands(a))



