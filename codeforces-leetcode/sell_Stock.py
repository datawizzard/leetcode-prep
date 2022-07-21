import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# profit=0
# for i in range(len(prices)-1):
#     profit+=max(0,prices[i+1]-prices[i])
#     print(profit)
# print(profit)
# class Solution:
#     def rotate(self, nums,k):
#         n=len(nums)
#         return (nums[n-k:]+nums[:n-k])
# nums=list(map(int,input().split()))
# k=int(input())
# x=Solution()
# print(x.rotate(nums,k)))
from collections import Counter

def intersect(num1,num2):
# items = (Counter(nums1) & Counter(nums2)).items()
# print(items)
# for k, v in items:
#     result += [k]*v
# print(result)
	return (Counter(nums1)&Counter(nums2)).elements()
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
m=len(nums1)
n=len(nums2)
result = []
print(Counter(nums1))
print(Counter(nums2))
print(intersect(nums1,nums2))


