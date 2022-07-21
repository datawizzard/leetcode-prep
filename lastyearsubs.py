import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	s=input()
	p="2020"
	flag=0
	if s[:4]==p:
		flag=1
	elif s[n-4:]==p:
		flag=1
	elif s[0]=="2" and s[n-3:]=="020":
		flag=1
	elif s[:2]=="20" and s[n-2:]=="20":
		flag=1
	elif s[:3]=="202" and s[n-1:]=="0":
		flag=1
	if flag:
		print("YES")
	else:
		print("NO")




