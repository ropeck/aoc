#!/usr/bin/python3
import aocd
from collections import deque
from copy import deepcopy
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
      robot = m.group(1)
      cost = {}
      for item in m.group(2).strip().split(" and "):
        (count, name) = item.split(" ")
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

  @property
  def names(self):
    return self.robots.keys()

  def can_build(self, r):
    # check if inv has materials listed in blueprint
    for n, v in self.blueprint.bp[r].items():
      if self.inv[n] < v:
        return False
    return True

  def collect_robot_work(self):
      for r in self.names:
        self.inv[r] += self.robots[r]

  def build(self, r):
    if not self.can_build(r):
      return False
    ns = deepcopy(self)
    for n, v in self.blueprint.bp[r].items():
      ns.inv[n] -= v
    ns.robots[r] += 1
    ns.t += 1
    return ns
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

  q = deque([(State(bp[0]))])

  max_geode = 0
  while q:
    st = q.pop()
    if st.t > 24:
      max_geode = max(max_geode, st.inv['geode'])
      print(f'{st.inv} {max_geode} {st.history}')
      continue
    st.collect_robot_work()
    # estimate the most possible geodes from this point, and skip out if less than max found so far
    #   (max if time remaining made geodes, or if a new geode robot was made each time remaining?)
    #   how to calculate geodes made and geode robots over time. it's an integral over each minute stepwise

    for r in st.names:
      if st.can_build(r):
        q.append(st.build(r))
    # or just wait
    st.t += 1
    st.history.append(None)
    q.append(st)



if __name__ == '__main__':
  main(len(sys.argv) > 1)
