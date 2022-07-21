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

# problem A

# n,h,x = MI()
# t = LI()
# for i in t:
# 	if i + x >= h:
# 		print("yes")
# 		break;
# else:
# 	print("no")

# problem B

# for _ in range(II()):
# 	s = I()
# 	c = 0
# 	s = s.split("0")
# 	for i in s:
# 		if i != '':
# 			c += 1
# 	print(c)

# problem C

# for _ in range(II()):
# 	c = II()
# 	d = int((math.log((c),2)) + 1)
# 	# print(d)
# 	a = 2**(d - 1) - 1
# 	b = a ^ c
# 	# print(a)
# 	print(a * b)


# problem D
for _ in range(II()):
	n = II()
	a = LI()
	c = 0
	flag = 0
	a.sort()
	for i,j in enumerate(a):
		# print(i,j)
		if j > i + 1:
			flag = 1
			break;
		else:
			c += i + 1 - j
	if c % 2 == 0 or flag == 1:
		print("Second")
	else:
		print("First")


# problem e

# for _ in range(II()):
# 	n,e,h,a,b,d = MI()
# 	s ,c ,chocmilk_left,omlette_left= 0,0,0,0
# 	if e < n and h < n:
# 		print(-1)
# 	else:
# 		x = min(a,b,d)
# 		if x == a:
# 			noofomo = 0
# 			omlette = e
# 			while omlette > 1:
# 				c += 1
# 				noofomo += 1
# 				omlette = omlette - 2
# 				if c == n:
# 					break;
# 			omlette_left = e % 2
# 			s = s + noofomo*a
# 			# print(s)
# 			if b < d:
# 				noofchoco = 0
# 				chocmilk = h
# 				while chocmilk > 2:
# 					c += 1
# 					noofchoco += 1
# 					chocmilk = chocmilk - 3
# 					if c == n:
# 						break;
# 				chocmilk_left = h % 3
# 				s += noofchoco*b
# 				# print(s)
# 				nofcake = 0
# 				if omlette_left > 0 and chocmilk_left > 0:
# 					c += 1
# 					nofcake += 1
# 					omlette_left = omlette_left - 1
# 					chocmilk_left -= 1
# 					s += nofcake*d
# 					if c < n:
# 						break;
# 			elif d >= b:
# 				nofcake = 0
# 				if omlette_left > 0 and chocmilk_left > 0:
# 					c += 1
# 					nofcake += 1
# 					omlette_left = omlette_left - 1
# 					chocmilk_left -= 1
# 					s += nofcake*d
# 					if c == n:
# 						break;
# 				else:
# 					noofchoco = 0
# 					chocmilk = h
# 					while chocmilk > 2:
# 						c += 1
# 						noofchoco += 1
# 						chocmilk = chocmilk - 3
# 						if c == n:
# 							break;
# 					chocmilk_left = h % 3
# 					s += noofchoco*b
# 		if x == b:
# 			noofchoco = 0
# 			chocmilk = h
# 			while chocmilk > 2:
# 				c += 1
# 				noofchoco += 1
# 				chocmilk = chocmilk - 3
# 				if c == n:
# 					break;
# 			chocmilk_left = h % 3
# 			s += noofchoco*b
# 			# print(s)
# 			if a < d:
# 				noofomo = 0
# 				omlette = e
# 				while omlette > 1:
# 					c += 1
# 					noofomo += 1
# 					omlette = omlette - 2
# 					if c == n:
# 						break;
# 				omlette_left = e % 2
# 				s = s + noofomo*a
# 				# print(s)
# 				nofcake = 0
# 				if omlette_left > 0 and chocmilk_left > 0:
# 					c += 1
# 					nofcake += 1
# 					omlette_left = omlette_left - 1
# 					chocmilk_left -= 1
# 					s += nofcake*d
# 					if c < n:
# 						break;
# 			elif d >= a:
# 				nofcake = 0
# 				if omlette_left > 0 and chocmilk_left > 0:
# 					c += 1
# 					nofcake += 1
# 					omlette_left = omlette_left - 1
# 					chocmilk_left -= 1
# 					s += nofcake*d
# 					if c == n:
# 						break;
# 				else:
# 					noofomo = 0
# 					omlette = h
# 					while omlette > 1:
# 						c += 1
# 						noofomo += 1
# 						noofomo = noofomo - 2
# 						if c == n:
# 							break;
# 					omlette_left = e % 3
# 					s += noofchoco*a
# 		if x == d:
# 			nofcake = 0
# 			chocmilk = h
# 			omlette = e
# 			while chocmilk > 0 and omlette > 0:
# 				c += 1
# 				nofcake += 1
# 				chocmilk = chocmilk - 1
# 				omlette = omlette - 1
# 				if c == n:
# 					break;
# 			chocmilk_left = h - nofcake
# 			omlette_left = e - nofcake
# 			s += nofcake * d
# 			if e < h:
# 				if h -	
# 		print(s)





	
