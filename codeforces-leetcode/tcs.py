import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
ranks=[0,0,0,0,0]
places=['Malaysia',  'Australia', 'Germany', 'Dubai', 'France']
flag=0
for i in range(0,5):
 if flag==1:
  break
 for j in range(0,5):
  r=input()
  if r.isnumeric():
   r=int(r)
   if r>0 and r<=5:
    if r==1:
     ranks[j]+=1
   else:
    flag=1
    break
  else: 
   flag=1
   break
print(ranks)
if flag==1:
 print("INVALID INPUT")
else:
 comb=list(zip(ranks,places))
 comb.sort(key = lambda x:x[0],reverse=True)
 print(comb)
 top=comb[0][0]
 for i in range(0,5):
  if top==comb[i][0]:
   print (comb[i][1])