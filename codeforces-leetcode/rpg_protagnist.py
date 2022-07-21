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
	p,f = MI()
	cnts,cntw = MI()
	s,w = MI()
	if s>w:
	    s,w=w,s
	    cnts,cntw =cntw,cnts
	ans=0
	for i in range(cnts):
		if i*s>p:
			continue;
		sf=i
		ss=min(f//s,cnts-i)
		left_f=p-(sf*s)
		left_s=f-(ss*s)
		wf=min(cntw,left_f//w)
		ws=min(left_s//w,cntw-wf)
		ans=max(ans,sf+ss+wf+ws)
	print(ans)