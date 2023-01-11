#!/usr/bin/python3
import aocd
from collections import deque
from copy import deepcopy
from pprint import pprint
import re
import sys

class State:
  def __init__(self, valves, cv):
    self.valves = valves
    self.t = 0
    self.opened = []
    self.cv = cv
    self.p = []
    self.flow = 0

  def flow_rate(self):
    return sum([self.valves[v].rate for v in self.opened])

  def open_valve(self):
    x = deepcopy(self)
    if self.cv in self.opened:
      return None
    x.opened.append(x.cv)
    x.t += 1
    x.flow += x.flow_rate()
    return x

  def go(self, tunnel):
    x = deepcopy(self)
    x.t += 1
    x.flow += x.flow_rate()
    x.p.append(x.cv)
    x.cv = tunnel
    return x

class Valve:
  def __init__(self, line):
    m = re.match("Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", line)
    if not m:
      print("Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)")
      print("line mismatch: " + line)
      return
    self.name = m.group(1)
    self.rate = int(m.group(2))
    self.v = m.group(3).split(", ")
    self.open = False

  def __repr__(self):
    return f'<Valve {self.name} {self.rate}->{",".join(self.v)}>'

def main(test=False):
  p = []
  mod = aocd.models.Puzzle(year=2022, day=16)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
  v = {}
  for l in data.splitlines():
    n = Valve(l)
    v[n.name] = n

  q = deque([State(v, "AA")])
  seen = []
  while q:
    print(f'--- {len(q)}')
    # for i in q:
    #   print(i)
    st = q.pop()
    if st.cv in seen:
      print(f'seen: {st.cv}')
      continue
    # seen.append(st.cv)
    if st.t >= 30:
      print(f'timed out: {st.p}')
      continue
    ov = st.open_valve()
    if ov:
      print(f'{st.t} open {st.cv}')
      q.append(ov)
    for n in v[st.cv].v:
      print(f'{st.t} go {n}')
      q.append(st.go(n))
      # print("queue")
      # print(q)
  return v


if __name__ == '__main__':
  main(len(sys.argv) > 1)
