import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, ceil
from collections import defaultdict as dd
from collections import Counter as cc
from bisect import bisect_left as bl
from bisect import bisect_right as br
import functools
INF = float('inf')
MOD = 998244353
mod = 10**9+7
sys.setrecursionlimit(100000000)
def inp(): return sys.stdin.readline().rstrip("\n")
def out(var):     sys.stdout.write(s(var) + "\n")  
def I():    return (inp())
def II():    return (int(inp()))
def FI():    return (float(inp()))
def SI():    return (list(s(inp())))
def MI():    return (map(int,inp().split()))
def LI():    return (list(MI()))
def SLI():    return (sorted(LI()))
def MF():    return (map(float,inp().split()))
def LF():    return (list(MF()))
def SLF():    return (sorted(LF()))
def min_swaps(t):
	s=list(t)
	# print(s)
	left, right = 0, len(s)-1
	center=False
	count=0
	while left < right:
		search=right
		while s[search] != s[left]:
			search -=1
		if search == left:
			# print("gg")
			if center and s[search].islower():
				return "Impossible"
			else:
				center=True
				middle_idx=len(s)//2
				while search != middle_idx:
					s[search],s[search+1]=s[search+1], s[search]
					count+=1
					search+=1
				s[middle_idx]=s[middle_idx].upper()
				# print(s)
		else:
			while search != right:
				# print(s)
				s[search],s[search+1] = s[search+1], s[search]
				# print(s,search)
				count += 1
				search += 1
			left += 1
			right -= 1
	return count
while True:
	t=I()
	if t=="0":
		break;
	l=min_swaps(t)
	r=min_swaps(t[::-1])
	print(min(l,r))

# 2nd Method

# def is_permutation_of_palindrome(s):
#     s = s.lower()
#     bit_vector = 0 << 25

#     for char in s:
#         index = ord(char) - 97
#         bit_vector = (1 << index) ^ bit_vector

#     return (bit_vector - 1) & bit_vector == 0



# def solution(s):
#     if is_permutation_of_palindrome(s):
#         s = list(s)
#         i, j = 0, len(s) - 1
#         total_swaps = 0

#         while j > i:
#             k = j
#             while k > i and s[i] != s[k]:
#                 k -= 1

#             while k < j:
#                 s[k], s[k + 1] = s[k + 1], s[k]
#                 total_swaps += 1
#                 k += 1

#             i += 1
#             j -= 1

#         return total_swaps
#     else:
#         return "Impossible"
        

# while True:
#     s=input().strip()
#     if s[0]=='0':
#         break
#     print(solution(s))



