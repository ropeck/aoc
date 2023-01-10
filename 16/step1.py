#!/usr/bin/python3
import aocd
from collections import deque
from copy import copy
from pprint import pprint
import re
import sys

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
  pprint(v)

  p = []
  q = deque([(0, v['AA'], [], [], 0)])
  while q:
    print(f'--- {len(q)}')
    # for i in q:
    #   print(i)
    (t, c, o, p, score) = q.pop()
    print(f'{t} {c} {o} {p[:3]} {score}')
    if t >= 30:
      print(f'timed out: {p}')
      continue
    # add current score
    # open a valve maybe or move
    for n in c.v:
      print(f'append {v[n].name} {p[:3]} {c.name}')
      q.append((t+1, v[n], o, copy(p + [v[n].name]), score))
      # print("queue")
      # print(q)
  return v


if __name__ == '__main__':
  main(len(sys.argv) > 1)
