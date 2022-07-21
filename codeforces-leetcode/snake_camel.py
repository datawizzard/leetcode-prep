import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=input()
	arr = [n[0].lower()]
	arr1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for letter in n[1:]: 
		if letter in (arr1): 
			arr.append('_')
			arr.append(letter.lower()) 
		else: 
			arr.append(letter)
	print(''.join(arr))