
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappush, heappop, heapify, nlargest, nsmallest

import os
import sys
sys.setrecursionlimit(1<<30)
from io import BytesIO, IOBase
import math
import bisect
from math import inf
import random
ins = lambda: [int(x) for x in input()]
inp = lambda: int(input())
inps = lambda: [int(x) for x in input().split()]
from fractions import Fraction as F

md=pow(10,9)+7
 
N = 2*(10**5) + 7
lvl=[-1]*N
c=[0]*N
p=[0]*N
ft=[0]*N
time=[0]
ar=[0]*N

st=[0]*(N+10)
end=[0]*(N+10)

def upd(i,v):
    while i<N:
        ft[i]+=v
        i+=i&(-i)


def query(i):
    r=0
    while i:
        r+=ft[i]
        i-=i&(-i)



def dfs2(cur,p,dc):
    st[cur]=time[-1]
    time[-1]+=1
    
    for nbr in dc[cur]:
        if nbr!=p:
            dfs2(nbr,cur,dc)
            c[cur]+=c[nbr]    
    end[cur]=time[-1]



def bfs(dc,cur):
    q=deque()
    q.append((cur,1))
    while q:
        nd,l =q.popleft()
        
        lvl[nd]=l
      #  print(nd,"**")
        for nbr in dc[nd]:
            if lvl[nbr]!=-1:
                continue
            p[nbr]=nd
            lvl[nbr]=l+1
            q.append((nbr,l+1))


dp=[[1]*N for _ in range(int(math.log2(N))+1)]


#dp2=[1]*(1000001)

def lca(e1,e2):
    l1,l2=lvl[e1],lvl[e2]
    if e1==e2:
        return e1
        
    if l1>l2:
        e1,e2=e2,e1
    
    dif=abs(l2-l1)
    po=0
    while dif:
        if dif&1:
            e2=dp[po][e2]
        
        po+=1
        dif>>=1
    # print(e1,e2,"#",lvl[e1],lvl[e2])
    if e1==e2:
        return e1
    

    lg=int(math.log2(N))+1
    for i in range(lg-1,-1,-1):
        if dp[i][e1]!=dp[i][e2]:
            e1=dp[i][e1]
            e2=dp[i][e2]
            #  print(e1,e2)
    return (dp[0][e1])

def main():
    n,q=inps()
    #a=inps()
    dc=defaultdict(list)
    for i in range(2,n+1):
        a,b =inps()
        dc[a].append(b)
        dc[b].append(a)
    p[1]=1
    bfs(dc,1)
    for i in range(1,n+1):
        dp[0][i]=p[i]

    dp[0][1]=1
    for i in range(1,int(math.log2(N))+1):
        for j in range(2,n+1):
            dp[i][j]=dp[i-1][dp[i-1][j]]

    for i in range(q):  
        e1,e2=inps()
        lc=lca(e1,e2)
        #print(lc)a
        c[e1]+=1
        c[e2]+=1
        c[lc]-=1
        if lc!=1 :
            c[p[lc]]-=1
        
    dfs2(1,-1,dc)
    for i in range(1,n+1):
        print(c[i],end=" ")


BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
if __name__ == "__main__": 
    main()
# import threading,sys
# sys.setrecursionlimit(1000000)
# threading.stack_size(1024000)
# thread=threading.Thread(target=main)
# thread.start()
