from collections import defaultdict
import sys

def dfs(v):
    component[v] = num_components
    visited[v] = True
    for w in D[v]:
        if visited[w] == False:  # посещён ли текущий сосед?
            dfs(w)

D = defaultdict(list)
tmp = defaultdict(list)

n = int(sys.stdin.readline().strip())
for i in range(n):
  inp = sys.stdin.readline().strip()
  A = list(map(int, inp.split()))
  D[A[0]].append(A[1])
  D[A[1]].append(A[0])

versh = []
for i in D:
  versh.append(i)

j = len(versh)

component = {}  # для каждой вершины храним номер её компоненты
num_components = 0

visited = {}
visited = dict.fromkeys(versh, False)
for v in versh:
  if not visited[v]:
    dfs(v)
    num_components += 1  

m = int(sys.stdin.readline())

for i in range(m):
  flag = 0
  res = []
  inp = sys.stdin.readline().strip()
  needFile = list(map(int, inp.split()))
  inp = sys.stdin.readline().strip()
  haveFile = list(map(int, inp.split()))
  for item in haveFile:
    if (component[item] == component[needFile[0]]):
      flag += 1
      res.append(str(item))
  print(str(flag) + " " + ' '.join(res))