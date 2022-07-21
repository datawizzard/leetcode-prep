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
for _ in range(II()):
	n = II()
	x = []
	y = []
	for i in range(n):
		p1,p2 = MI()
		x.append(p1)
		y.append(p2)
	x.sort()
	y.sort()
	if n % 2 == 1:
		print(1)
	else:
		print((x[n//2] - x[(n-1)//2] + 1) * (y[n//2] - y[(n-1)//2] + 1))


# <iframe src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2Ffacebook%2F&tabs=timeline&width=340&height=1500&small_header=false&adapt_container_width=true&hide_cover=false&show_facepile=true&appId"
#              width="340" height="100%" style={{border:"none",overflow:"hidden"}} scrolling="no" frameborder="0" allowTransparency="true" allow="encrypted-media">
#             </iframe>