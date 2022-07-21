import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
nums=list(map(int,input().split()))
i=1
while i<len(nums):
	if nums[i]==nums[i-1]:
	    nums.pop(i)
	    print(nums,i)
	else:
	    i+=1
print(len(nums))