#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 19

class Workflow:
  def __init__(self, str):
    m = re.match(r"(.*){(.*)}", str)
    if not m:
      raise ValueError
    self.name, rules = m.groups()
    self.rules = [Condition(x) for x in rules.split(",")]

class Condition:
  def __init__(self, str):
    self.str = str
    m = re.match(r"(.*)([<>])(.*):(.*)", str)
    if m:
      self.var, self.op, n, self.target = m.groups()
      self.n = int(n)
    else:
      self.op = None
      self.target = str
  def __repr__(self):
    return f"<{self.str}>"


def main(test):
  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()
  workflows = []
  while True:
    line = data.pop(0)
    if not line:
      break
    workflows.append(Workflow(line))
  


  print("total", total)
  if not test:
    aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
