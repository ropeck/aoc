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
      return m.group(1)

    number = parse_line("Monkey", regexp=" (.*):")
    if number == None:
      return None
    m = Monkey()
    m.number = number
    m.items = re.split(",\s", parse_line("Starting items"))
    m.operation = parse_line("Operation")
    m.test = parse_line("Test")
    m.if_true = parse_line("If true: throw to monkey", regexp=" (.*)")
    m.if_false = parse_line("If false: throw to monkey", regexp=" (.*)")
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
  for m in monkey:
    print(m)
  print(monkey)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
