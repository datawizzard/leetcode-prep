import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	k=input()
	n=float(k)
	j=1
	while float(pow(float(j),17.0))<=n:
		j+=1
	print(j-1)