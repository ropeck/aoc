#!/usr/bin/python3
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

def main(path):
  v = {}
  with open(path,"r") as fh:
    for n in [Valve(l) for l in fh]:
      v[n.name] = n
  pprint(v)
  return v


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
