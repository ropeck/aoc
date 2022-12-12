#!/usr/bin/python3
import re
import sys

def debug(str):
  # debug(str)
  pass

class Monkey():
  """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
  """
  def __init__(self):
    self.number = None
    self.items = []
    self.operation = None
    self.test = None
    self.if_true = None
    self.if_false = None

  def __str__(self):
    return """Monkey {}:
  Starting items: {}
  Operation: {}
  Test: {}
    If true: throw to monkey {}
    If false: throw to monkey {}""".format(
      self.number, ", ".join(self.items), self.operation, self.test, self.if_true, self.if_false)

  def __repr__(self):
    return "<Monkey {} [{}]>".format(self.number, ", ".join(self.items))

  def parse_fh(fh):
    def parse_line(label="", regexp=None):
      l = fh.readline().strip()
      if not l:
        return None
      if not regexp:
        regexp = ':\s?(.*)'
      expanded_regexp = label + regexp
      m = re.match(expanded_regexp, l)
      if not m:
        raise ValueError("expecting '{}' but found '{}'".format(expanded_regexp, l))
      return m.group(1)
    def parse_if_line(cond):
      return int(parse_line("If {}: throw to monkey".format({True: "true", False: "false"}[cond]), regexp=" (.*)"))
    def parse_items_line():
      return re.split(",\s", parse_line("Starting items"))

    monkey = parse_line("Monkey", regexp=" (.*):")
    if monkey == None:
      return None
    m = Monkey()
    m.number = int(monkey)
    m.items = parse_items_line()
    m.operation = parse_line("Operation")
    m.test = parse_line("Test")
    m.if_true = parse_if_line(True)
    m.if_false = parse_if_line(False)
    l = fh.readline()
    return m

def main(path):
  monkey = []
  with open(path, "r") as fh:
    while True:
      m = Monkey.parse_fh(fh)
      if m:
        monkey.append(m)
      else:
        break

  round = 0
  while round < 20:
    round += 1
    for m in monkey:
      for i in m.items:
        m.thing = "foo"

  for m in monkey:
    print(m)
  print(monkey)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
