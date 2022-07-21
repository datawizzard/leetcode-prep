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
class Boutique:
	def __init__(self,boutiqueId,boutiqueName,boutiquetype,boutiquerating,boutiquepoints):
		self.boutiqueId =boutiqueId
		self.boutiqueName = boutiqueName
		self.boutiquetype = boutiquetype
		self.boutiquerating = boutiquerating
		self.boutiquepoints = boutiquepoints
class OnlineBoutique:
	def __init__(self,boutiquedict):
		self.boutiquedict = boutiquedict
	def getBoutique(self,lower,upper,extra,typo):
		m,x,y = [],[],[]
		m = self.boutiquedict.get(typo)
		if m == None:
			return None
		for i in m:
			if lower <= i.boutiquerating <=upper:
				i.boutiquepoints += extra
		
		for i in m:
			x.append(i.boutiquepoints)
		x.sort(reverse =True)
		for i in x:
			for j in m:
				if i == j.boutiquepoints:
					y.append(j)
		return y
if __name__ == '__main__':
		no = int(input())
		boutiquelist = []
		for i in range(no):
			boutiqueId = int(input())
			boutiqueName = input()
			boutiquetype = input()
			boutiquerating = float(input())
			boutiquepoints = II()
			boutiquelist.append(Boutique(boutiqueId,boutiqueName,boutiquetype,boutiquerating,boutiquepoints))
		lower = float(input())
		upper = float(input())
		extra = int(input())
		typo = input()
		tablelist = []
		for i in boutiquelist:
			tablelist.append(i.boutiquetype)
		tablelist = set(tablelist)
		boutiquedict = {}
		for i in tablelist:
			new_list = []
			for j in boutiquelist:
				if i == j.boutiquetype:
					new_list.append(j)
			boutiquedict[i] = new_list
			new_list = []
		obj = OnlineBoutique(boutiquedict)
		res = obj.getBoutique(lower,upper,extra,typo)
		if res == None:
			print("No boutique found")
		else:
			for i in res:
				print(i.boutiqueId,i.boutiqueName,i.boutiquepoints)
