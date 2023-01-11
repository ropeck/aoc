#!/usr/bin/python3
import aocd
from collections import deque
import functools
import re
import sys

def main(test=False):
  mod = aocd.models.Puzzle(year=2022, day=16)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
  flow = {}
  tunnels = {}
  for l in data.splitlines():
    m = re.match("Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", l)
    name = m.group(1)
    tunnels[name] = m.group(3).split(", ")
    flow[name] = int(m.group(2))

  active = []   # valves that are nonzero
  dist = {}
  for valve in flow:
    if valve != "AA" and not flow[valve]:
      continue
    if valve != "AA":
      active.append(valve)
    dist[valve] = {valve: 0, "AA": 0}
    visited = {valve}
    q = deque([(0, valve)])

    while q:
      d, curr = q.popleft()
      for n in tunnels[curr]:
        if n in visited:
          continue
        visited.add(n)
        if flow[n]:
          dist[valve][n] = d + 1
        q.append((d + 1, n))
    del dist[valve][valve]
    if valve != "AA":
      del dist[valve]["AA"]

  ind = {}
  for i, v in enumerate(active):
    ind[v] = i

  @functools.cache
  def dfs(t, v, opened):
    maxval = 0
    for n in dist[v]:
      b = 2 ** ind[n]
      if opened & b:
        continue
      timeleft = t - (dist[v][n] + 1)
      if timeleft > 0:
        maxval = max(maxval, dfs(timeleft, n, opened | b) + flow[n] * timeleft)
    return maxval

  print(dfs(30, "AA", 0))

if __name__ == '__main__':
  main(len(sys.argv) > 1)
