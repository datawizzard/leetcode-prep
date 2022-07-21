import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
lenchar = 26
def check(cnt,k): 
	v = 0
	for i in range(lenchar): 
		if cnt[i] > 0: 
			v += 1
	return (k >= v)  
def unique(s): 
	u = 0 
	n = len(s)  
	cnt = [0] * lenchar 
	for i in range(n): 
		if cnt[ord(s[i])-ord('a')] == 0: 
			u += 1
		cnt[ord(s[i])-ord('a')] += 1 
	cstart = 0
	cend = 0
	mlen = 1
	mstart = 0
	cnt = [0] * len(cnt) 

	cnt[ord(s[0])-ord('a')] += 1 
	for i in range(1,n): 
		cnt[ord(s[i])-ord('a')] += 1
		cend+=1
		while check(cnt, 2) == False: 
			cnt[ord(s[cstart])-ord('a')] -= 1
			cstart += 1
		if cend-cstart+1 > mlen: 
			mlen = cend-cstart+1
			mstart = cstart 

	return s[mstart:mstart + mlen] 
return unique(s) 
s = "abbccc"
print(unique(s))
