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

cache = {}


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
    return list(self.robots.keys())

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
    global cache
    if not self.can_build(r):
      return False
    key = (self.t, r, str(self.inv), str(self.robots))
    if key in cache:
      return deepcopy(cache[key])

    ns = deepcopy(self)
    for n, v in self.blueprint.bp[r].items():
      ns.inv[n] -= v
    ns.robots[r] += 1
    ns.history.append(r)
    ns.t += 1
    ns.collect_robot_work()
    cache[key] = ns
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
  max_st = q[0]
  while q:
    st = q.pop()
    if st.t > 24 or st.inv["geode"] + 3 * (24 - st.t) < max_geode:
      if st.inv['geode'] > max_geode:
        max_geode = st.inv['geode']
        max_st = st
      print(f'{st.robots} {st.inv["geode"]} {max_geode} {st.history}')
      continue
    # estimate the most possible geodes from this point, and skip out if less than max found so far
    #   (max if time remaining made geodes, or if a new geode robot was made each time remaining?)
    #   how to calculate geodes made and geode robots over time. it's an integral over each minute stepwise

    def avg(s):
      return sum(s) / len(s)
    building = False
    for r in reversed(st.names):
      if st.can_build(r) and st.robots[r] <= avg(st.robots.values())+1.5:
        q.append(st.build(r))
        building = True
    # or just wait
    if not building:
      st.t += 1
      st.history.append(None)
      st.collect_robot_work()
      q.append(st)

  print("")
  print(f'{max_st.history}\n{max_st.inv} {max_st.robots}')


if __name__ == '__main__':
  main(len(sys.argv) > 1)
