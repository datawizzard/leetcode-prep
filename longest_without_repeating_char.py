import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def lonrep(s):
	#Method 1
	# if len(s)==0:
	# 	return 0
	# t=set()
	# i,j,m=0,0,0
	# while i<len(s):
	# 	p=s[i]
	# 	while p in t:
	# 		t.remove(s[j])
	# 		j+=1
	# 	t.add(p)
	# 	m=max(m,i-j+1)
	# 	i+=1
	# return m

	# Method 2 
	# word_map = {}
    
	# start = longest = 0
    
	# for idx, char in enumerate(s):
	    
	#     if char in word_map and start <= word_map[char]:
	#         start = word_map[char] + 1
	        
	#     else:
	#         longest = max(longest, idx - start  + 1 )
	#     print(word_map)    
	#     word_map[char] = idx
	    
	    
	# return longest

	# Here, we are planning to implement a simple sliding window methodology 

# def longestUniqueSubsttr(s): 
	
	# Creating a set to store the last positions of occurrence 
	# seen = {} 
	# maximum_length = 0

	# # starting the inital point of window to index 0 
	# start = 0
	
	# for end in range(len(s)): 

	# 	# Checking if we have already seen the element or not 
	# 	if s[end] in seen: 

	# 		# If we have seen the number, move the start pointer 
	# 		# to position after the last occurrence 
	# 		start = max(start, seen[s[end]]+1) 

	# 	# Updating the last seen value of the character 
	# 	seen[s[end]] = end
	# 	maximum_length = max(maximum_length, end-start + 1) 
	# return maximum_length 
	d={}
	i,j,ans=0,0,0
	for j in range(len(s)):
		if s[j] in d:
		    i=max(i,d[s[j]]+1) #This step is done to if we find 
		    			# s[j] in d ,i will equal to value of prev
		    			# value of that key and max will ensure that
		    			# prev value of i only stored in new_i when 
		    			# prev i should not be less than current i       
		d[s[j]]=j
		ans=max(ans,j-i+1)
		print(j,i,ans)
	return ans

s=input()
print(lonrep(s))
