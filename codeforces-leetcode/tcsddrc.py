import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
s=[]
t=[]
n=int(input())
for i in range(n):
	inp=input()
	if inp!='q':
		if float(inp)>0.0:
			s.append(inp)
	else:
		print("False Input")
		break;
	if i>=n-1:
		for j in s:
			if j!=42.953:
				t.append(float(j))
		t.sort()
		print(t[-1:-4:-1])

