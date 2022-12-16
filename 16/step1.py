#!/usr/bin/python3
from pprint import pprint
import re
import sys
from copy import copy

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

def main(path):
  v = {}
  with open(path,"r") as fh:
    for n in [Valve(l) for l in fh]:
      v[n.name] = n
  pprint(v)

  p = []
  q = [(0, v['AA'], [], [], 0)]
  while q:
    print("---")
    for i in q:
      print(i)
    (t, c, o, p, score) = q.pop()
    print(f'{t} {c} {o} {p} {score}')
    if t >= 30:
      break
    # add current score
    # open a valve maybe or move
    for n in c.v:
      print(f'append {v[n].name} {p} {c.name}')
      q.append((t+1, v[n], o, p + [copy(c)], score))


  return v


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
