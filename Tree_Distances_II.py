import sys
input = sys.stdin.readline
n=int(input())
gr=[[] for i in range(n)]
for i in range(n-1):
	x,y=map(int,input().split())
	gr[x-1].append(y-1)
	gr[y-1].append(x-1)
for i in range(n):
	if len(gr[i])==1:break
p=i
par=[-1 for j in range(n)]
sub={}
deg={}
for j in range(n):
	sub[j]=0
deg[i]=0
s=[i]
par[i]=i
m=[]
ans=0
while s:
	x=s.pop()
	m.append(x)
	ans+=deg[x]
	for j in gr[x]:
		if j==par[x]:continue
		par[j]=x
		deg[j]=deg[x]+1
		s.append(j)
for i in range(n-1,-1,-1):
	if par[m[i]]==m[i]:continue
	sub[par[m[i]]]+=sub[m[i]]+1
 
an={}
an[p]=ans
for i in range(1,n):
	x=m[i]
	d=sub[x]
	l=n-2-d
	an[x]=an[par[x]]+l-d
 
for j in range(n):
	print(an[j],end=' ')