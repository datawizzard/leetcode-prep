import sys
import math
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

n=int(input())
ans=i=0
j=n-1
diff=[]
p=[]
j=n-1
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
zip_object = zip(list1,list2)
for list1_i, list2_i in zip_object:
	diff.append(list1_i-list2_i)
print(diff)
diff.sort()
print(diff)
while(i<j):
	if diff[i]+diff[j]>0:
		ans+=j-i
		j=j-1
	else:
		i+=1
print(ans)
