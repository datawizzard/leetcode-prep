import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
flag=0
def switch(h) : 
    return { 
        0 : "Saturday", 
        1 : "Sunday", 
        2 : "Monday", 
        3 : "Tuesday", 
        4 : "Wednesday", 
        5 : "Thursday", 
        6 : "Friday", 
    }[h] 
def whatdate(day, month, year) : 
    if (month == 1): 
        month = 13
        year = year - 1
  
    if (month == 2) : 
        month = 14
        year = year - 1
    q = day 
    m = month 
    k = year % 100; 
    j = year // 100;
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j 
    h = h % 7
    print(switch (h))
day,month,year=map(int,input().split("-"))
def isLeap(year):
    if ((year% 4==0) and (year%100 !=0)) or (year % 400 == 0):
        return 1
if (year > 2099 or year< 1600):
    flag=1 
if (month < 1 or month > 12):
    flag=1 
if (day< 1 or day > 31): 
    flag=1 
if (month == 2):
    if (isLeap(year)!=1 and day>28):
        flag=1 
if (month == 4 or month == 6 or month == 9 or month== 11):
    if day>30:
        flag=1
if flag==1:
    print("Invalid date")
else:
    whatdate(day,month,year)