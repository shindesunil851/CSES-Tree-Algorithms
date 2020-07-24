
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

dp=[0]*(1000001)

dp2=[1]*(1000001)
#dp2=[1]*(1000001)

def dfs(dc,cur,p):
    dp[cur]=0
 #   dp2[cur]=0
    

    for nbr in dc[cur]:
        if nbr==p:
            continue
        dfs(dc,nbr,cur)
        dp[cur]=max(dp[nbr]+1,dp[cur])
        #dp2[cur]+=dp2[nbr]
        #print("node",cur," with it ",dp[cur],"  without ",dp2[cur])
   # print("node",cur," depth ",dp[cur])


def dfs2(dc,cur,p,n,partial):
    
    pre=[]
    suf=[]

    for nbr in dc[cur]:
        if nbr!=p:
            pre.append(dp[nbr])
            suf.append(dp[nbr])

    for i in range(1,len(pre)):
        pre[i]=max(pre[i-1],pre[i])
    
    for i in range(len(suf)-2,-1,-1):
        suf[i]=max(suf[i],suf[i+1])
    

        
    cn=0
    for nbr in dc[cur]:
        if nbr!=p:
            m1=-inf
            m2=-inf
            
            if cn:
                 m1=pre[cn-1]

            if cn<len(suf)-1:
                m2=suf[cn+1]

            newp=1+max([partial,m1,m2])
            
            dfs2(dc,nbr,cur,n,newp)
            cn+=1
    dp[cur]=max(pre[-1] if pre else -1,partial)

def main():
    n=inp()
    #a=inps()
    dc=defaultdict(list)
    for i in range(1,n):
        a,b=inps()
        dc[a].append(b)
        dc[b].append(a)
    
    dfs(dc,1,-1)
    dfs2(dc,1,-1,n,-1)

    for i in range(1,n+1):
        print(dp[i]+1,end=" ")
    


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
