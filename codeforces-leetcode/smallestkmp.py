import sys
import math
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def addedge(edge,u,v):
	edge[u].append[v]
	edge[v].append[u]
def dfs(u,edge,visited):
	visited[u]=True
	for i in range(len(edge[u])):
		if visited[edge[u][i]]==False:
			dfs(edge[u][i],edge,visited)
def isp(n):
	if n==1:
		return False
	if n==2:
		return True
	for i in range(0,math.sqrt(n)+1):
		if n%i==0:
			if i*i==n:
				ans+=1
			else:
				ans+=2
	if ans>0:
		return False
	else:
		return True
for _ in range(int(input())):
	s=input()
	p=input()
	k=""
	a=[0]*26
	b=[0]*26
	for i in range(0,len(s)):
		a[s[i]-'a']+=1
		b[s[i]-'a']+=1
	for i in range(0,len(p)):
		a[s[i]-'a']-=1
	for i in range(0,26):
		if (i+'a')==p[0]:
			while len(k)<len(p):
				while b[i]>0 and len(k)<len(p):
					k+=chr(i+'a')
					b[i]=b[i]-1
				i+=1
				if i==26:
					break
	for i in range(0,26):
		if k>p and chr(i+'a')==p[0]:
			print(p)
		while(a[i]>0):
			print(chr(i+'a'))
			a[i]=a[i]-1
		if k<=p and chr(i+'a')==p[0]:
			print(p)



