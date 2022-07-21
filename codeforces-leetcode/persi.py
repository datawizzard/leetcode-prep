import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
arr=list(map(str,input().split(" ")))
c=0
alpha=["a","e","i","o","u","A","E","I","O","U"]
for i in arr:
	if i not in alpha:
		c+=1
print(c)



	