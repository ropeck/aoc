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
    self.test_str = None
    self.if_true = None
    self.if_false = None
    self.inspections = 0
  def inspect(self):
    self.inspections += 1

  def item_list_str(self):
    return ", ".join([str(x) for x in self.items])

  def inspection_info(self):
    return f'Monkey {self.number} inspected items {self.inspections} times.'

  def __str__(self):
    return """Monkey {}:
  Starting items: {}
  Operation: new = old {}
  Test: {}
    If true: throw to monkey {}
    If false: throw to monkey {}""".format(
      self.number, self.item_list_str(), self.operation, self.test_str, self.if_true, self.if_false)

  def __repr__(self):
    return "<Monkey {} [{}]>".format(self.number, self.item_list_str())

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
      return [int(i) for i in re.split(",\s", parse_line("Starting items"))]

    monkey = parse_line("Monkey", regexp=" (.*):")
    if monkey == None:
      return None
    m = Monkey()
    m.number = int(monkey)
    m.items = parse_items_line()
    m.operation = parse_line("Operation: new = old", regexp=" (.*)")
    (m.op_cmd, m.op_val) = m.operation.split()
    if m.op_cmd not in "+*":
      raise ValueError(f'{self.op_cmd} operation not found')
    if m.op_val != "old":
      m.op_val = int(m.op_val)
    m.test_str = parse_line("Test")
    mm = re.match("divisible by (.*)", m.test_str)
    m.test_divisible = int(mm.group(1))
    m.if_true = parse_if_line(True)
    m.if_false = parse_if_line(False)
    l = fh.readline()
    return m

  def operate(self, old):
    if self.op_val == "old":
      n = old
    else:
      n = self.op_val
    if self.op_cmd == "+":
      return n + old
    if self.op_cmd == "*":
      return n * old

  def next_monkey(self, old):
    if old % self.test_divisible == 0:
            return self.if_true
    else:
      return self.if_false

  def append_item(self, i):
    self.items.append(i)
    print(f'{self.__repr__()} append {i}')

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
    print(f'== ROUND {round} ==')
    for m in monkey:
      items = m.items
      m.items = []
      for i in items:
        m.inspect()
        print('')
        print(f'{m.number} item {i}')
        new = m.operate(i)
        new = int(new / 3)
        next = m.next_monkey(new)
        monkey[next].append_item(new)
    print('')

  for m in monkey:
    print(m.inspection_info())
  print(monkey)
  mb = 1

  insp = [i.inspections for i in monkey]
  insp.sort()

  for i in insp[-2:]:
    print(f'{mb} {i}')
    mb = mb * i
  print(f'monkey business: {mb}')

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
