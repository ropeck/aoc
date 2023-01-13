#!/usr/bin/python3
import aocd
from collections import deque
from dataclasses import dataclass
import re
import sys

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3


class Blueprint:
  def __init__(self, line):
    self._name = {'ore': ORE, 'clay': CLAY, 'obsidian': OBSIDIAN, 'geode': GEODE}
    self._item = {}
    for k, v in self._name.items():
      self._item[v] = k
    line = line.strip()
    line = line.replace(".", "")
    p = line.split("Each ")
    m = re.match("Blueprint (\\d+): ", p[0])
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


class State:
  def __init__(self, blueprint):
    self.t = 1
    self.blueprint = blueprint
    self.inv = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
    self.robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
    self.next_robot = None
    self.history = []

  def can_build(self, r):
    # check if inv has materials listed in blueprint
    return False

  def collect_robot_work(self):
    pass

  def build(self, r):
    if not self.can_build(r):
      return False
    # decrease the material count, increase the robot count
    # return state in t+1


def main(test):
  mod = aocd.models.Puzzle(year=2022, day=19)
  if not test:
    data = mod.input_data
  else:
    data = ""
    for line in mod.example_data.splitlines():
      if not line:
        data += "\n\n"
      else:
        data += line + " "
  bp = []
  for line in data.split("\n\n"):
    bp.append(Blueprint(line))
  print(bp)

  b = bp[0]
  st = State(b)

  q = deque()

  t = 1
  while t<=24:
    nr = []
    pos = []
    for r, ri in b.bp.items():
      build = True
      for i in ri:
        if st.inv[i] < ri[i]:
          build = False
          break
      if st.can_build(r) and st.robots[r] < 2 or min(st.robots) > 0:
        pos.append(r)

    if pos:
      pos.reverse()
      print(f'possible: {pos}')
      r = pos[0]
      ri = b.bp[r]
      print(f'build {r} robot with {ri}')
      st.build(r)

    for r, c in enumerate(robot.inv):
      mat.incr(r, c)
    if pos:
      for r in nr:
        robot.incr(r)
    print(f'end of {t}: {mat} {robot}')
    t+=1


if __name__ == '__main__':
  main(len(sys.argv) > 1)
