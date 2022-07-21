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
	a,b = MI()
	s = I()
	x = s.count("0")
	y = s.count("1")
	a -= x
	b -= y
	i , j = 0,a+b-1
	while i <= j:
		if s[i] == s[j]:
			i += 1
			j -= 1
		elif s[i] == '?' and s[j] == "?" and a > 0:
			list1 = list[s]
			list1[i] = "0"
			list1[j] = "0"
			s = "".join(list1)
			a -= 1
		elif s[i] == '?' and s[j] == "?" and b > 0:
			list1 = list[s]
			list1[i] = "1"
			list1[j] = "1"
			s = "".join(list1)
			b -= 1
		elif (s[i] == "?" and s[j] == "1") or (s[i] == "1" and s[j] == "?"):
			if b > 0:
				list1 = list[s]
				list1[i] = "0"
				list1[j] = "0"
				s = "".join(list1)
				b -= 1
			else:
				break;
		elif (s[i] == "?" and s[j] == "0") or (s[i] == "0" and s[j] == "?"):
			if a > 0:
				s[i] = s[i].replace("?","0")
				a -= 1
			else:
				break;
	if s == s[::-1]:
		print(s)
	else:
		print(-1)

