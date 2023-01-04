#!/usr/bin/python3
import os
#import snoop
from icecream import ic
import sys
import tkinter

class Tower:
  def __init__(self, has_graphics=True):
    self.t = []   # each row is a byte
    self.rocks = self.read_rocks()
    self.pending_rocks = self.rocks.copy()

    self.rock_n = 0
    self.jet = self.read_jets()
    self._next_jet = []
    self.has_graphics = has_graphics
    if self.has_graphics:
      self.screen = tkinter.Tk()
      self.screen.geometry("200x1200")
      self.canvas = tkinter.Canvas(self.screen, width=100, height=1150)
      self.canvas.pack()
      self.screen.update_idletasks()
      self.screen.update()

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
      t = self.t
    # draw the top 10 rows of the tower.
    # indicate the bottom and next rock position
    dx = dy = 10
    n = min([len(t), 100])
    b = 15
    h = n * dy + b*2
    w = b * 2 + 7 * dy
    c = self.canvas

    c.create_rectangle(0, 0, 100, 1150, fill="white")
    c.create_rectangle(b, h - b - (n * dy), w - dy, h - b,
                                   outline="black", fill="light gray")

    for row_num, row in list(enumerate(t)):
      if row == 255:
        continue
      for nn in range(6,-1,-1):
        if row & 2**nn:
          x = b + dx*nn
          y = b + dy*row_num
          c.create_rectangle(x, y, x + dx, y + dy, outline="black", fill="blue")
    if r:
      ic(i, r)
      for j, rock_row in enumerate(r):
        for nn in range(7):
          x = b + dx * nn
          y = b + dy * rock_row + i
          if rock_row&2**nn:
            c.create_rectangle(x, y, x + dx, y + dy, outline="black", fill="green")

    c.create_rectangle(b, h - b - (n * dy), w - dy, h - b,
                                   outline="black", fill=None)
    self.screen.update_idletasks()
    self.screen.update()
  def overlap(self, rock, i, tower):
    for j, rr in enumerate(rock):
      tr = i + j
      if tr > len(tower) - 1:
        return True
      o = tower[tr] & rock[j]
      if o:
        return True
    return False

  def draw_rock(self, rock):
    print("--",rock,"--")
    for r in rock:
      print(bin(128|r))
    print("")

  def drop(self):
    # start at top + 3, then apply jets and move down until stopped
    # self.t + [0, 0, 0]
    # loop from top down, check to see if the rock overlaps
    # use binary AND of the tower with the rock - if (rock & tower top ) != 0 then it's colliding
    l, m = self.next_rock()
    m.reverse()
    r = (l, m)
    current_rock = [row << (5 - r[0]) for row in r[1]]
    tower = [0 for i in current_rock] + [0, 0, 0] + self.t
    i = 0
    while True:
      if i > len(tower)+1:
        break
      self.draw(tower, i, current_rock)
      # apply jet to current_rock position
      print("row",i)
      jet = self.next_jet()
      if jet == 1:
        print("jet right")
        if not self.rock_side(current_rock, 0):
          new_rock = [r >> 1 for r in current_rock]
          if not self.overlap(new_rock, i, tower):
            current_rock = new_rock
      else:
        print("jet left")
        if not self.rock_side(current_rock, 6):
          new_rock = [r << 1 for r in current_rock]
          if not self.overlap(new_rock, i, tower):
            current_rock = new_rock
      self.draw(tower, i, current_rock)
      if self.overlap(current_rock, i+1, tower):
        print("Rock falls 1 unit, causing it to come to rest")
        break
      i += 1
      print("Rock falls 1 unit")
    self.draw(tower, i, current_rock)
    for n, rock_row in enumerate(current_rock):
      pos = i + n
      tower[pos] = tower[pos] | rock_row
    self.draw(tower, i)
    self.t = [row for row in tower if row]
    print("---")

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
    print(n)
    t.drop()
    t.draw()
    n += 1
  print(f'height: {t.height()}')
  t.screen.mainloop()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path, 2022)
