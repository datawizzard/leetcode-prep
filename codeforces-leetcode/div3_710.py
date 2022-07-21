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
for _ in range(II()):
	n,k = MI()
	s = I()
	ans = 0
	for i in range(n):
		if s[i] == '*':
			# print("fg")
			s = s[:i] + "x" + s[i+1:]
			ans += 1
			break;
	# print(s)
	for j in range(n-1,-1,-1):
		if s[j] == '*':
			s = s[:j] + "x" + s[j+1:]
			ans += 1
		if s[j] == 'x':
			break;
	# print(s,ans)
	if j - i <= k:
		print(ans)
	else:
		# print(j,i)
		# print(s[i+1:j])
		i = i + k
		while i  < j:
			if s[i] == '*':
				ans += 1
			else:
				while s[i] != '*':
					i = i - 1
				ans += 1
			i += k
		print(ans)