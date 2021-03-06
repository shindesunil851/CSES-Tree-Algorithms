
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

# dp=[1]*(1000001)

# dp2=[1]*(1000001)


#using dfs leads tle in python
def dfs(dc,cur,p,mx):

    l=1
    
    for nbr in dc[cur]:
        if nbr==p:
            continue
        l1=1+dfs(dc,nbr,cur,mx)

        mx[-1]=max(l1+l-2,mx[-1])
        l=max(l,l1)
    #print("cur ",cur," l ",l,mx)
    return l

def bfs(dc,cur,lv,ml):
    vis=[0]*N
    q=deque([(cur,0)])
    while q:
        nd,lvl=q.popleft()
        lv[0]=nd
        vis[nd]=1
        ml[0]=max(ml[0],lvl+1)
        for nbr in dc[nd]:
            if vis[nbr]==0:
                q.append((nbr,lvl+1))
                



def main():
    n=inp()
    #a=inps()
    dc=defaultdict(list)
    for i in range(1,n):
        a,b=inps()
        dc[a].append(b)
        dc[b].append(a)
    mx=[0]
    lv=[-1]
    ml=[-1]
    #fs(dc,1,-1,mx)
    #print(mx[-1])
    bfs(dc,1,lv,ml)

    bfs(dc,lv[0],lv,ml)
    print(ml[0]-1)

    


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
