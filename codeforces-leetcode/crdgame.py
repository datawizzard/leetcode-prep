import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	cf,rk=map(int,input().split())
	ans=0
	ans1=0
	flag=0
	if cf%9==0:
		ans=cf//9+1
	else:
		ans=math.ceil(cf/9)
	if rk%10==0:
		ans1=rk//+1
	else:
		ans1=math.ceil(rk/9)
	if ans>ans1:
		flag=1
		print("%s %s"%(flag,ans1))
	elif ans==ans1:
		flag=1
		print("%s %s"%(flag,ans))
	elif ans<ans1:
		flag=0
		print("%s %s"%(flag,ans))


