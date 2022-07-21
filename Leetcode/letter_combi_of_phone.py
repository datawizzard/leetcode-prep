import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
for _ in range(II()):
	digit = I()
	res = []
	digitarray = {
	"2":"abc",
	"3":"def",
	"4":"ghi",
	"5":"jkl",
	"6":"mno",
	"7":"pqrs",
	"8":"tuv",
	"9":"wxyz"
	}
	def phonenumber(i,currentstr):
		if len(currentstr) == len(digit):
			res.append(currentstr)
			return 
		for c in digitarray[digit[i]]:
			phonenumber(i+1,currentstr + c)
		phonenumber(0,"")
	return res

