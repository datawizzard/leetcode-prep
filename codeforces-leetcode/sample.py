import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
I= [3,4,5,6]
print(list(map(lambda x:(x/3==2),I)))
