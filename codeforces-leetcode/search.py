import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
m=int(input())
mat=[]
mat = [[int(input()) for x in range (n)] for y in range(m)]