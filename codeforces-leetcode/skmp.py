import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
t = int(input())
for i in range(t):
    string = input().strip()
    pattern = input().strip()
    sostring = sorted(string)
    sopattern = sorted(pattern)
    print(sostring)
    print(sopattern)
    patternli = [x for x in pattern]
    newlist = []
    j = 0
    m = int(len(sopattern))
    for i in sostring:
        if j<m:
            if i==sopattern[j]:
                j+=1
                continue
            else:
                newlist.append(i)
                print(newlist)
        else:
            newlist.append(i)
            print(newlist)
    result=[]
    for i in range(int(len(newlist))):
        if pattern[0]<newlist[i]:
            result = newlist[:i] + patternli + newlist[i:]
            break
        else:
        	result=newlist+patternli
    print(''.join(str(x) for x in result))