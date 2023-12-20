#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 19

class Workflow:
  def __init__(self, str):
    self.str = str
    m = re.match(r"(.*){(.*)}", str)
    if not m:
      raise ValueError
    self.name, rules = m.groups()
    self.rules = [Condition(x) for x in rules.split(",")]
  
  def apply(self, part):
    pass
    for r in self.rules:
      if r.op is None:
        return r.target
      v = part.rating[r.var]
      if r.op == "<":
        if v < r.n:
          return r.target
      if r.op == ">":
        if v > r.n:
          return r.target
    raise ValueError
      


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

class Part:
  def __init__(self, str):
    m = re.match(r"{(.*)}", str)
    r = {}
    for a in m.group(1).split(","):
      k,v = a.split("=")
      r[k] = int(v)
    self.rating = r

  def sum(self):
    return sum(self.rating.values())
    

def main(test):
  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()
  workflows = {}
  while True:
    line = data.pop(0)
    if not line:
      break
    w = Workflow(line)
    workflows[w.name] = w
  
  total = 0
  while data:
    line = data.pop(0)
    p = Part(line)

    wf = 'in'
    s = [wf]
    while wf not in ['R', 'A']:
      w = workflows[wf]
      wf = w.apply(p)
      s.append(wf)

    print(" -> ".join(s), p.sum())
    if wf == 'A':
      total += p.sum()
    
  
  print("total", total)
  if not test:
    aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
