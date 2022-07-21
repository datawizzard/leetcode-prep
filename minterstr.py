import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=input()
ans=n.replace('1','')+'2'
t=ans.find('2')
print(ans[:t]+'1'*n.count('1')+ans[t:-1])