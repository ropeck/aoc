#!/usr/bin/python3
import sys

class Tower:
  def __init__(self):
    self.t = [255]   # each row is a byte
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

  def draw(self, t=None, i=None, r=None):
    if not t:
      t=self.t
    t.reverse()
    print(f'{r} {i} {t}')
    for row in t:
      if row == 255:
        continue
      s=""
      for n in range(7):
        nn = 7-n
        m=2**nn
        #import pdb; pdb.set_trace()
        #print(f'  {i} {nn} {i-nn}')
        if (r and (i-n<=0) and (n >= i-len(r) and n <= i) and m & r[i-n]):
          s += "@"
        elif (m & row):
          s += "#"
        else:
          s += "."
      print(f'|{s}|')
    print('+-------+')
    print('')

  def drop(self):
    # start at top + 3, then apply jets and move down until stopped
    # self.t + [0, 0, 0]
    # loop from top down, check to see if the rock overlaps
    # use binary AND of the tower with the rock - if (rock & tower top ) != 0 then it's colliding
    r = self.next_rock()
    print(f'rock: {r}')
    current_rock = [row << int((7 - r[0]) / 2) for row in r[1]]
    print(f'centered {current_rock}')
    tower = self.t + [0, 0, 0, 0] 
    tower.reverse()
    print(list(enumerate(tower)))
    for i in range(len(tower)):
      d=tower.copy()
      d.reverse()
      self.draw(d, i, current_rock)
      # apply jet to current_rock position
      jet = self.next_jet()
      if jet == 1:
        print("jet right")
        if not self.rock_side(current_rock, 0):
          current_rock = [r >> 1 for r in current_rock]
      else:
        print("jet left")
        if not self.rock_side(current_rock, 6):
          current_rock = [r << 1 for r in current_rock]
      print(f'current: {i} {current_rock}  t:{tower}')
      if tower[i+1] & current_rock[0]:
        print('rock: ' + str(current_rock))
        print(f' {tower[i+1]} {current_rock[0]} {tower[i+1] & current_rock[0]}')
        print('overlap next')
        break
    for n, rock_row in enumerate(current_rock):
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
  #  t.draw()
    n += 1
  print(f'height: {t.height()}')


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path, 2022)
