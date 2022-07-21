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
class Movie:
	def __init__(self,movie_id,movie_name,ticketcost):
		self.movie_id = movie_id
		self.movie_name = movie_name
		self.ticketcost = ticketcost
	def name_assign_Price_Category(self,ticketcost):
		ticketCategory = ""
		if ticketcost > 0 and ticketcost < 150:
			ticketCategory += "General"
		elif ticketcost >= 150 and ticketcost < 250:
			ticketCategory += "Silver"
		elif ticketcost >= 250 and ticketcost < 350:
			ticketCategory += "Gold"
		else:
			ticketCategory += "Platinum"
		return ticketCategory
class Movie_Ticket:
	def __init__(self,customer_name,movie_name,viewerCount,totalTicketCost):
		self.customer_name = customer_name
		self.movie_name = movie_name
		self.viewerCount = viewerCount
		self.totalTicketCost = totalTicketCost
def getCategoryWiseCount(self,MovieList):
	d = {}
	for i in self.MovieList:
		x = self.name_assign_Price_Category(i.ticketcost)
		if x not in d:
			d[x] = 1
		else:
			d[x] += 1
	return d
def bookMovieTicket(self,MovieList,c_name,m_name,viewerCount):
	for i in self.MovieList:
		if i.movie_name == c_name:
			return {c_name,i.ticketcost * viewerCount}
if __name__== "__main__":
	n = int(input())
	MovieList = []
	for i in range(n):
		movie_id = input()
		movie_name = input()
		ticketcost = input()
		MovieList.append(Movie(movie_id,movie_name,ticketcost))
	# print(documentList)
	
	c_name = input()
	m_name = input()
	viewerCount = int(input())
	x = getCategoryWiseCount(MovieList)
	print("Category wise ticket count")
	print(x)
	y = bookMovieTicket(MovieList,c_name,m_name,viewerCount)
	if y == None:
		print("Movie Not Available")
	else:
		print(y)


