import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
s=input()
if len(s)>20:
	print("Wrong Input")
else:
	d={}
	for i in s:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1
	for i in d:
		if d[i]==1:
			print(i)
			break;
	else:
		print("Exceptional Number")