import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def decbil(n): 
    return bin(n).replace("0b","")
for _ in range(int(input())):
	n=int(input())
	x=decbil(n)
	#print(x)
	a=0
	b=0
	c=len(x)-1
	for i in range(len(x)):
		if x[i]=="1":
			a+=1
	for i in range(len(x)-1,-1,-1):
		if x[i]=="1":
			b=len(x)-i-1
			break;
	#print(a,b,c)
	print("%s#%s#%s"%(a,b,c))

