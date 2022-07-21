import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=input()
arr1=list(n)
count=0
for i in arr1:
	if i!=' ' or i!='"':
		print(i,end="")
	elif i=='"':
		count+=1
		print(i,end="")
		continue
	elif i==' ':
		print()
