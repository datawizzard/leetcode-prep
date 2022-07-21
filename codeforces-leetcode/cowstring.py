import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
from collections import Counter
s = input().strip()
cnt = Counter()
cnt2 = Counter()
for c in s:
    cnt[c]+=1
#print(cnt)
mx = max(cnt.values())
#print(mx)
for c in s:
    cnt[c]-=1
    for d,v in cnt.items():
        cnt2[c+d]+=v
        print(cnt2)
#print(cnt2)
print(max(mx,max(cnt2.values())))
