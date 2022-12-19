#!/usr/bin/python3
import re
import sys

ORE=0
CLAY=1
OBSIDIAN=2
GEODE=3

class Blueprint:
  def __init__(self, line):
    self._name={'ore': ORE, 'clay': CLAY, 'obsidian': OBSIDIAN, 'geode': GEODE}
    self._item={}
    for k,v in self._name.items():
      self._item[v] = k
    line = line.strip()
    line = line.replace(".","")
    p = line.split("Each ")
    m = re.match("Blueprint (\d+): ", p[0])
    self.number = m.group(1)
    self.bp = {}
    for e in p[1:]:
      m = re.match("(.*) robot costs (.*)", e)
      if not m:
        print(e)
        exit(1)
      robot = self._name[m.group(1)]
      cost = {}
      for item in m.group(2).strip().split(" and "):
        (count, name) = item.split(" ")
        name = self._name[name]
        cost[name] = int(count)
      self.bp[robot] = cost


  def __repr__(self):
    return f'<Blueprint {self.number} {self.bp}>'


def main(path):
  bp = []
  with open(path, "r") as fh:
    for line in fh:
      bp.append(Blueprint(line))
  print(bp)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
