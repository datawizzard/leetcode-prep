import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	l=0
	a,b=input().split()
	for i in range(int(a)):
		arr=list(map(str,input().split()))
		if arr[0]=="CONTEST_WON":
			if int(arr[1])<20:
				l=l+300+(20-int(arr[1]))
			else:
				l=l+300
		elif arr[0]=="TOP_CONTRIBUTOR":
			l=l+300
		elif arr[0]=="BUG_FOUND":
			if int(arr[1])>=50 and int(arr[1])<=1000:
				l=l+int(arr[1])
		elif arr[0]=="CONTEST_HOSTED":
			l=l+50
		else:
			l=0
	if b=="INDIAN":
		print(l//200)
	else:
		print(l//400)
