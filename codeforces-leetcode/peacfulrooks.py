import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, ceil
from collections import defaultdict as dd
from collections import Counter as cc
from bisect import bisect_left as bl
from bisect import bisect_right as br
import functools
 
sys.setrecursionlimit(100000000)
t= lambda : int(input())
intinp = lambda: int(input().strip())
stripinp = lambda: input().strip()
fltarr = lambda: list(map(float,input().strip().split()))
arr = lambda: list(map(int,input().strip().split()))
# for _ in range(t()):
# 	n,m=map(int,input().split())
# 	arr=[-1]*(n+1)
# 	vis=[True]*(n+1)
# 	for i in range(m):
# 		x,y = [int(k) for k in input().split()]
# 		if x!=y:
# 			vis[x]=False
# 			arr[x]=y
# 	vis[0]=True
# 	ans=0
# 	for i in range(n+1):
# 		if vis[i]==False:
# 			start=arr[i]
# 			vis[i]=True
# 			count=1
# 			while vis[start]==False:
# 				vis[start]=True
# 				count+=1
# 				start=arr[start]
# 				if start==i:
# 					count+=1
# 			ans+=count
# 	print(ans)
def dfs(start):
	global r,c,vis,temp,cycle
	stack=[]
	print(start)
	stack.append(start)
	while len(stack):
		s=stack.pop()
		if not vis[s]:
			temp+=1
			vis[s]=1
			print(vis[s],s)
		if s[0] in c and s[1] in r:
			if not vis[(c[s[0]],s[0])]:
				print((c[s[0]],s[0]))
				stack.append((c[s[0]],s[0])) # 1,2
			if not vis[(s[1],r[s[1]])]:
				print((s[1],r[s[1]]))
				stack.append((s[1],r[s[1]]))
		else:
			if s[0] in c:
				if not vis[(c[s[0]], s[0])]:
					stack.append((c[s[0]], s[0]))
			if s[1] in r:
				if not vis[(s[1], r[s[1]])]:
					stack.append((s[1], r[s[1]]))
			cycle=0
			print(cycle)
t = int(input())
for _ in range(t):
	n,m=map(int,input().split())
	arr=[]
	r={}
	c= {}
	vis={}
	for i in range(m):
		x,y=map(int,input().split())
		r[x]=y
		c[y]=x
		arr.append((x,y))
		print(r)
		print(c)
		print(arr)
		vis[(x,y)]=0
	count=0
	ans=0
	for i in arr:
		if i[0]==i[1] or vis[i]==1:
			continue
		temp=0
		start=i
		cycle=1
		dfs(start)
		if cycle:
			ans+=temp+1
		else:
			ans+=temp
	print(ans)
# int main() {
# 	int a, b, n, m, o, p, t, x, y, c;
# 	cin >> p;
# 	for (int r = 0; r < p; r++){
# 	    cin >> n >> m;
# 	    vector <int> s (n+1);
# 	    for (int i = 0; i < m; i++){
# 	        cin >> a >> b;
# 	        s[a] = b;
# 	    }
# 	    vector <int> used (n+1);
# 	    for (int i = 1; i <= n; i++){
# 	        if (used[i] == 0){
# 	            used[i] = 1;
# 	            if (s[i] == i) m--;
# 	            else {
# 	                c = s[i];
# 	                while (c > 0){
# 	                    used[c] = 1;
# 	                    if (c == i){
# 	                        m++;
# 	                        break;
# 	                    }
# 	                    c = s[c];
# 	                }
# 	            }
# 	        }
# 	    }
# 	    cout << m << "\n";
# 	}
# 	return 0;
# }
#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define rep(i,a,b) for(int i = a; i < b; i++)
 
# using namespace std;
 
# typedef vector<int> vi;
# typedef vector<long long> vll;
# typedef long long ll;
# typedef double dd;
 
# int main(void){
# #ifndef ONLINE_JUDGE
# 	freopen("input.txt", "r", stdin);
# 	freopen("output.txt", "w", stdout);
# #endif
#   int t;
#   cin>>t;
#   while(t--){
#     int n,m;
#     cin>>n>>m;
#     vector<pair<int,int>> c(m);
#     int r = 0, f = 0;
#     vi g(n+1);
#     rep(i,0,m) {
#       cin>>c[i].fi>>c[i].se;
#       if(c[i].fi == c[i].se) r++;
#       g[c[i].fi] = c[i].se;
#     }
#     int s = 0;
#     rep(i,1,n+1) {
#       if(g[i] == 0 || g[i] == i) continue;
#       if(!s)s = i;
#       int n = g[i];
#       g[i] = i;
#       while(n != 0 && n != g[n]) {
#         int k = n;
#         n = g[n];
#         g[k] = k;
#         if(n == s) {
#           f++;
#           break;
#         }
#       }
#       s = 0;
#     }
#     cout<<m+f-r<<endl;
#   }
# }