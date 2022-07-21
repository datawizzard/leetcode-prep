import sys,io,os
I = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

I = lambda: input().encode()
for _ in range(int(I())):
	n,m = map(int, I().split())
	rows = [list(map(int,I().split())) for _ in range(n)]
	cols = [list(map(int,I().split())) for _ in range(m)]
	for c in cols:
		if rows[0][0] not in c:
			continue
		d = {r[0]: r for r in rows}
		for q in c:
			print(*d[q])