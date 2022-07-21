import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# import sys
# import math
# def input(): return sys.stdin.readline().strip("\n")
# def I():    return (input())
# def II():    return (int(input()))
# def MI():    return (map(int,input().split()))
# def LI():    return (list(map(int,input().split())))
# class Document:
# 	def __init__(self,docId,docName,docDetails):
# 		self.docId = docId
# 		self.docName = docName
# 		self.docDetails = docDetails
# class DocumentArchive:
# 	a = []
# 	def __init__(self,archiveId,documentList):
# 		self.archiveId = archiveId
# 		self.documentList = documentList
# 	def findDateFromDocumentDetails(self,documentList):
# 		a = []
# 		# print(documentList)
# 		for i in self.documentList:
# 			# print(i.docDetails)
# 			z = i.docDetails.split(",")
# 		# print(z)
# 			for j in z:
# 				if j.find('/') != -1:
# 					a.append((i.docId,j))
# 					break;
# 		return a
# 	def countDocumentOfGivenType(self,docType):
# 		count = 0
# 		for i in self.documentList:
# 			if docType == i.docName.split(".")[1]:
# 				count += 1
# 		return count

# if __name__== "__main__":
# 	n = int(input())
# 	documentList = []
# 	for i in range(n):
# 		docId = input()
# 		docName = input()
# 		docDetails = input()
# 		documentList.append(Document(docId,docName,docDetails))
# 	# print(documentList)
	
# 	docType = input()
# 	obj = DocumentArchive(1,documentList)
# 	x = obj.findDateFromDocumentDetails(documentList)
# 	# print(x)
# 	if len(x) > 0:
# 		for i,j in x:
# 			print(i,j)
# 	y = obj.countDocumentOfGivenType(docType)
# 	print("Document Count = ",y)

import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
class Apparel:
	def __init__(self,apparelbrand,types,price,instock):
		self.apparelbrand = apparelbrand
		self.types = types
		self.price = price
		self.instock = instock
class Store:
	a = []
	def __init__(self,apparelList):
		self.documentList = documentList
	def checkavail(self,brand,types,size,noofreq):
		a = []
		# print(documentList)
		for i in self.apparelList:
			if i.brand == brand and i.types == types:
				return True
			if i.noofreq <=
			for j in self.instock:
				if i.size == j.values():
				return True

		return False
	def countDocumentOfGivenType(self,docType):
		count = 0
		for i in self.documentList:
			if docType == i.docName.split(".")[1]:
				count += 1
		return count

if __name__== "__main__":
	n = int(input())
	apparelList = []
	for i in range(n):
		brand = input()
		types = input()
		price = input()
		t = int(input())
		d = {}
		for i in range(2*t):
			x.key = input()
			y.value = input()
			d.add(x.key,y.value)
		ApparelList.append(Apparel())
	# print(documentList)
	
	docType = input()
	obj = DocumentArchive(1,documentList)
	x = obj.findDateFromDocumentDetails(documentList)
	# print(x)
	if len(x) > 0:
		for i,j in x:
			print(i,j)
	y = obj.countDocumentOfGivenType(docType)
	print("Document Count = ",y)