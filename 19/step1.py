#!/usr/bin/python3
import re
import sys
from copy import copy, deepcopy

import aocd

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
  
  @property
  def names(self):
    return list(self._name.keys())

def shortrep(inv):
  ret = []
  for i,v in inv.items():
    n = i[0]
    if i == 'obsidian':
      n = i[1]
    ret.append(f'{n}:{v}')
  return " ".join(ret)


class State:
  def __init__(self, blueprint, t, inv=None, robots=None):
    self.blueprint = blueprint
    self.inv = inv or {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
    self.robots = robots or {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}



  def __repr__(self):
    return f'<State {self.t} i({shortrep(self.inv)}) r({shortrep(self.robots)})'

  @property
  def names(self):
    return list(self.robots.keys())

  def can_build(self, r):
    # check if inv has materials listed in blueprint
    for n, v in self.blueprint.bp[r].items():
      if self.inv[n] < v:
        return False
    return True

  def should_build(self, r):
    if r == 'geode':
      return True
    return self.robots[r] < max([b.get(r, 0) for b in self.blueprint.bp.values()])

  def collect_robot_work(self):
    for r in self.names:
      self.inv[r] += self.robots[r]

  def build(self, r):
    for b in self.blueprint.bp[r].keys():
      if not self.robots[b]:
        print(f'no {b} robots to build {r}')
        return self
    if not self.can_build(r) or not self.should_build(r):
      return self
    for n, v in self.blueprint.bp[r].items():
      self.inv[n] -= v
    self.collect_robot_work()
    self.robots[r] += 1
    return self

  def find_max_nodes(self, time_left, target=None):
    global cache
    key = (time_left, target, str(self.inv), str(self.robots))
    # if key in cache:
    #   return cache[key]
    self.t = time_left
    if time_left < 1:
      cache[key] = self
      return self
    next_states = []
    if target:
      for b in self.blueprint.bp[target].keys():
        if not self.robots[b]:
          return self
      while True:
        if self.can_build(target) and self.should_build(target):
          next_states = [self.build(target)]
          break
        self.collect_robot_work()
        self.t -= 1
        if self.t < 1:
          cache[key] = self
          return self

    for r in reversed(self.names):
      tgt_st = deepcopy(self)
      max_nodes = tgt_st.find_max_nodes(tgt_st.t, r)
      print(f'{tgt_st.t} {max_nodes} {r}')
      next_states.append(max_nodes)
    next_states.sort(key=lambda s: s.inv['geode'])
    if not next_states:
      cache[key] = self
      return self
    cache[key] = next_states[-1]
    return next_states[-1]


def find_max_geodes(d, bp, time_left, inv, robots, target):
  # print(f'find_max {d} {time_left} {target} {inv} {robots}')
  inv = copy(inv)
  robots = copy(robots)
  if target:
    while any([inv[i] < req for i, req in bp.bp[target].items()]):
      for i in inv.keys():
        inv[i] += robots[i]
      time_left -= 1
      if time_left <= 0:
        break
    if time_left <= 0:
      return (inv, robots)
    # print("target", target)
    if target == 'geode' or robots[target] < max(d.get(target, 0) for d in bp.bp.values()):
      if target == "geode":
        print(f'{time_left} build {target} {inv}')
      for i, req in bp.bp[target].items():
        inv[i] -= req
      for i in inv.keys():
        inv[i] += robots[i]
      robots[target] += 1
      time_left -= 1
      if time_left <= 0:
        return (inv, robots)
      # print(f'{time_left}       {target} {inv}')

  result = []
  for t in reversed(inv.keys()):
    # print(f'find_max {time_left} {target} {t} {inv} {robots}')
    geodes = find_max_geodes(d+1, bp, time_left - 1, inv, robots, t)
    result.append(geodes)
  result.sort(key=lambda i: i[0]['geode'])
  # print(result)
  inv, robots = result[-1]
  return inv, robots


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

  for target in reversed(bp[0].names):
    print("------------------------------------")
    print(target, find_max_geodes(0, bp[0], 24, {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0},
                                 {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}, target))


if __name__ == '__main__':
  main(len(sys.argv) > 1)
