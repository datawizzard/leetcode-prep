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
# def numberSorter(n):
# 	a = list(map(int, str(n)))
# 	a.sort(reverse = True)
# 	print(*a,sep="")
# n = int(input())
# numberSorter(n)
# import calendar
# month = int(input())
# day = int(input())
# number = calendar.weekday(2020,month,day)
# d =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
# print(d[number])

n = int(input())
a = [1, 2, 5, 11, 12, 15, 21, 22, 25, 51, 52, 55]
if n <= 12:
	print(a[((n-1)%12)])
else:
	a = a[3:]
	print(a[(n-13)])




