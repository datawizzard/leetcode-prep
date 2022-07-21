import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
arr=input()
d={}
for i in arr:
	d[i]=0
for i in arr:
	d[i]+=1
print(d)
