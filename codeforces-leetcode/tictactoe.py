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
	mat = [[i for i in input()] for i in range(3)]
	count_x ,count_o,count_ = 0,0,0
	for i in range(3):
		for j in range(3):
			if mat[i][j] == 'X':
				count_x += 1
			elif mat[i][j] == 'O':
				count_o += 1
			else:
				count_ += 1
	win_x ,win_y = 0,0
	if mat[0][0] == mat[0][1] == mat[0][2] == 'X':
		win_x = 1
	if mat[1][0] == mat[1][1] == mat[1][2] == 'X':
		win_x = 1
	if mat[2][0] == mat[2][1] == mat[2][2] == 'X':
		win_x = 1
	if mat[0][0] == mat[1][0] == mat[2][0] == 'X':
		win_x = 1
	if mat[0][1] == mat[1][1] == mat[2][1] == 'X':
		win_x = 1
	if mat[0][2] == mat[1][2] == mat[2][2] == 'X':
		win_x = 1
	if mat[0][0] == mat[1][1] == mat[2][2] == 'X':
		win_x = 1
	if mat[0][2] == mat[1][1] == mat[2][0] == 'X':
		win_x = 1


	if mat[0][0] == mat[0][1] == mat[0][2] == 'O':
		win_y = 1
	if mat[1][0] == mat[1][1] == mat[1][2] == 'O':
		win_y = 1
	if mat[2][0] == mat[2][1] == mat[2][2] == 'O':
		win_y = 1
	if mat[0][0] == mat[1][0] == mat[2][0] == 'O':
		win_y = 1
	if mat[0][1] == mat[1][1] == mat[2][1] == 'O':
		win_y = 1
	if mat[0][2] == mat[1][2] == mat[2][2] == 'O':
		win_y = 1
	if mat[0][0] == mat[1][1] == mat[2][2] == 'O':
		win_y = 1
	if mat[0][2] == mat[1][1] == mat[2][0] == 'O':
		win_y = 1
	# print(win_x,win_y)
	if (win_x == 1 and win_y == 1) or (count_x < count_o or count_x > count_o + 1):
		print(3)
	elif (count_x == count_o == 0 and count_ == 9) or (win_x == win_y == 0 and count_ > 0):
		print(2)
	elif (win_x == win_y == 0 and count_ == 0):
		print(1)
	elif (win_x == 1 and win_y == 0 and count_x > count_o) or (win_y == 1 and win_x == 0 and count_x == count_o):
		print(1)
	else:
		print(3)