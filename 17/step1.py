#!/usr/bin/python3
import sys

class Tower:
  def __init__(self):
    self.t = [0]   # each row is a byte
    self.rocks = self.read_rocks()
    self.pending_rocks = self.rocks.copy()

    self.rock_n = 0
    self.jet = self.read_jets()
    self._next_jet = []

  def read_jets(self):
    with open(path, "r") as fh:
      return fh.read().strip()

  def next_jet(self):
    if not self._next_jet:
      self._next_jet = list(self.jet)
      self._next_jet.reverse()
    r = self._next_jet.pop()
    return {'<': -1, '>': 1}[r]

  def height(self):
    return len(self.t)

  def next_rock(self):
    if not self.pending_rocks:
      self.pending_rocks = self.rocks.copy()
    r = self.pending_rocks.pop()
    # print(f'{r} pending: {self.pending_rocks}')
    return r

  def rock_side(self, r, i):
    for row in r:
      if row & 2**i:
        return True
    return False

  def drop(self):
    # start at top + 3, then apply jets and move down until stopped
    # self.t + [0, 0, 0]
    # loop from top down, check to see if the rock overlaps
    # use binary AND of the tower with the rock - if (rock & tower top ) != 0 then it's colliding
    r = self.next_rock()
    print(f'rock: {r}')
    current_rock = [row << int((6 - r[0]) / 2) for row in r[1]]
    tower = self.t + [0, 0, 0] + [0 for i in current_rock]
    tower.reverse()
    overlap = 0
    for i, row in enumerate(tower):
      if row & current_rock[0]:
        overlap = -1
        break
      # apply jet to current_rock position
      prev_rock = current_rock
      jet = self.next_jet()
      if jet == 1:
        if not self.rock_side(current_rock, 6):
          current_rock = [r << 1 for r in current_rock]
      else:
        if not self.rock_side(current_rock, 0):
          current_rock = [r >> 1 for r in current_rock]
    if not overlap:
      prev_rock = current_rock
    i += overlap
    for n, rock_row in enumerate(prev_rock):
      tower[i-n] = tower[i-n] | rock_row
    tower.reverse()
    self.t = [row for row in tower if row]
    print(self.t)
    print(self.height())
    # handle multiple line rocks
      # if overlap(tower, r, i):
      #   mark r
      #   break

  def read_rocks(self):
    rock_list = []
    with open("rocks","r") as fh:
      while True:
        r = []
        while True:
          l = fh.readline().strip()
          if not l:
            break
          w = len(l)
          byte = sum(2 ** i for i, v in enumerate(reversed([ch == "#" for ch in l])) if v)
          r.append(byte)
        if not r:
          rock_list.reverse()
          return rock_list
        r.reverse()
        rock_list.append((w, r))


def main(path, max_count):
  t = Tower()
  n=0
  while n <= max_count:
    t.drop()
    n += 1
  print(f'height: {t.height()}')


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path, 2022)
