import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

# Logic

#We don't know which floor would be the most optimal 
# floor to make the first attempt hence we are trying out all
#  the floors through the loop, also we do not know if 
#  dropping from a certain floor will cause the egg to
#  break or not so we are testing for both cases one in 
#  which we assume that the egg would break and in the other 
#  we assume that it won't, recursive calls with left over eggs 
#  and floors in both cases give us the number of attempts required.
#  But since the question asks us to assume the worst case we take
#  the possibility as a fact which requires greater number of 
#  attempts to find the critical floor. 

# In simpler terms, suppose if we are testing for the 3rd floor 
# then we check the number of attempts to find the critical floor
#  for both cases if the egg would break from the 3rd floor
#   and if the egg wont break from the 3rd floor, if it requires 
#   greater number of attempts to find the critical floor if the 
#   egg would break if dropped form the 3rd floor then we would 
#   assume that upon dropping from the 3rd floor the egg would 
#   actually break because we want the worst case here. Then we 
#   take the minimum of number of attempts required for finding 
#   the critical floor in worst case of all of the floors in our
#    range and that is the answer.
#  Recursive
def eggdropping(e,f):
	if f==0 or f==1:
		return f
	if e==1:
		return f
	ans=sys.maxsize
	for k in range(1,f+1):
		a = 1 + max(eggdropping(e-1,k-1),eggdropping(e,f-k))
		ans=min(ans,a)
	return ans
e,f=map(int,input().split())
print(eggdropping(e,f))

# Memoization
def eggdropping(e,f):
	if dp[e][f]!=-1:
		return dp[e][f]
	if f==0 or f==1:
		return f
	if e==1:
		return f
	ans=sys.maxsize
	for k in range(1,f+1):
		a = 1 + max(eggdropping(e-1,k-1),eggdropping(e,f-k))
		ans=min(ans,a)
		dp[e][f]=ans
	return dp[e][f]
e,f=map(int,input().split())
dp=[[-1 for j in range(51)] for i in range(110)]
print(eggdropping(e,f))

# Optimized Binary Search Approach : NlogK
def eggdropping(e,f):
	if dp[e][f]!=-1:
		return dp[e][f]
	if f==0 or f==1:
		return f
	if e==1:
		return f
	low,high,ans=1,f,float('inf')
	while low<=high:
		mid=(low+high)//2
		left=eggdropping(e-1,mid-1)
		right=eggdropping(e,f-mid)
		# here we are finding max because in question
		# it is asking to find min of worst case which 
		# always happens when maximum time taken.
		temp = 1 + max(left,right)
		# here 1 is adding to increase the count every time 
		# we attempts to break the egg.
		if left>=mid:
			high=mid-1
		else:
			low=mid+1
		ans=min(ans,temp)
		dp[e][f]=ans
	return dp[e][f]
e,f=map(int,input().split())
dp=[[-1 for j in range(51)] for i in range(11)]
print(eggdropping(e,f))

# N^2 solution
class Solution:
    def superEggDrop(self, egg: int, floor: int) -> int:
        dp = [[0]*(egg+1) for i in range(floor+1)]
        for i in range(1 , floor+1):
            for j in range(1 , egg + 1):
            	# there are two case arises
            	# when  we are moving fronm bottom to top either
            	# egg breaks or not if egg breaks we decrease egg count
            	# else not and 1 is incresing the number of attempt after
            	# every floor when egg breaks.
            	# dp[i-1][j-1] when egg breaks
            	# dp[i-1][j] when egg does not break.
                dp[i][j] =  1 + dp[i-1][j] + dp[i-1][j-1]
                if dp[i][j] >= floor:
                    return i
e,f=map(int,input().split())
dp=[[-1 for j in range(51)] for i in range(11)]
print(eggdropping(e,f))


