import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	s=input()
	n=len(s)
	d=set()
	for i in range(n):
		count,even,odd=0,0,0
		for j in range(i,n):
			if s[j]=='1':
				count+=1
			else:
				# print("g")
				if count%2==1:
					odd+=1
				else:
					even+=1
			l=j-i+1
			d.add((l,even,odd))
			# print(d)
	# print(d)
	print(len(d))

