# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
# for _ in range(II()):
# 	s = I()
# 	i = s.find("11")
# 	j = s.find("00")
# 	# print(i,j)
# 	if i != -1 and j != -1 and i < j:
# 		print("NO")
# 	else:
# 		print("YES")
for _ in range(II()):
	n = II()
	a = LI()
	alice ,bob,even_count,odd_count = 0,0,0,0
	a.sort(reverse= True)
	for i in range(n):
		if i % 2 == 0:
			if a[i] % 2 == 0:
				alice += a[i]
			else:
				alice += 0
		else:
			if a[i] % 2 == 1:
				bob += a[i]
			else:
				bob += 0
	# print(alice,bob)
	if alice > bob:
		print("Alice")
	elif bob > alice:
		print("Bob")
	else:
		print("Tie")