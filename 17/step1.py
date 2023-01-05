#!/usr/bin/python3
import os
#import snoop
from icecream import ic
import sys
import time
import tkinter

running = False

def keypress(event):
  global running

  running = True

class Tower:
  def __init__(self, has_graphics=True):
    self.t = []   # each row is a byte
    self.rocks = self.read_rocks()
    self.pending_rocks = []

    self.rock_n = 0
    self.jet = self.read_jets()
    self._next_jet = []

    self.border = 15
    self.dx = self.dy = 10
    self.has_graphics = has_graphics
    if self.has_graphics:
      self.screen = tkinter.Tk()
      self.screen.geometry("200x1200")
      self.canvas = tkinter.Canvas(self.screen, width=100, height=1150)
      self.screen.bind("<space>", keypress)
      self.canvas.pack()
      self.screen.update_idletasks()
      self.screen.update()

  def read_jets(self):
    with open(path, "r") as fh:
      return fh.read().strip()

  def next_jet(self):
    if not self._next_jet:
      self._next_jet = list(self.jet).copy()
      self._next_jet.reverse()
    r = self._next_jet.pop()
    return {'<': -1, '>': 1}[r]

  def height(self):
    return len(self.t)

  def peek_rock(self):
    if self.pending_rocks:
      return self.pending_rocks[-1]
    _, r = self.rocks[-1]
    return r

  def next_rock(self):
    if not self.pending_rocks:
      self.pending_rocks = [(n, r.copy()) for n, r in self.rocks]
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
    n = min([len(t), 100])
    h = n * self.dy + self.border*2
    w = self.border * 2 + 7 * self.dy
    if self.has_graphics:
      c = self.canvas
      b = self.border
      dx = self.dx
      dy = self.dy
      c.create_rectangle(0, 0, 100, 1150, fill="white")
      c.create_rectangle(b, h - b - (n * dy), w - b, h - b,
                                     outline="black", fill="light gray")

    for row_num, row in list(enumerate(t)):
      if row == 255:
        continue
      self.draw_row(row, row_num, "blue")
    if r and self.has_graphics:
      ic(i, r)
      for j, rock_row in enumerate(r):
        self.draw_row(rock_row, j + i, "green")
    if self.has_graphics:
      c.create_rectangle(b, h - b - (n * dy), w - b, h - b,
                                     outline="black", fill=None)
      self.screen.update_idletasks()
      self.screen.update()

  def draw_row(self, row, row_num, color):
    for nn in range(6, -1, -1):
      if row & 2 ** nn:
        self.draw_square(nn, row_num, color)

  def draw_square(self, nn, row_num, color):
    b = self.border
    dx = self.dx
    dy = self.dy
    x = b + dx * nn
    y = b + dy * row_num
    if self.has_graphics:
      self.canvas.create_rectangle(x, y, x + dx, y + dy, outline="black", fill=color)

  def overlap(self, rock, i, tower):
    rock = rock.copy()
    # rock.reverse()
    for j, rr in enumerate(rock):
      tr = i + j
      if tr >= len(tower):
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
    rock = r[1].copy()
    current_rock = [row << (5 - r[0]) for row in rock]
    tower = [0 for i in current_rock] + [0, 0, 0] + self.t
    i = 0
    while True:
      time.sleep(1)
      if i + len(current_rock) > len(tower):
        break
      self.draw(tower, i, current_rock)
      # apply jet to current_rock position
      # print("row",i)
      jet = self.next_jet()
      if jet == 1:
        # print("jet right")
        if not self.rock_side(current_rock, 0):
          new_rock = [r >> 1 for r in current_rock]
          if not self.overlap(new_rock, i, tower):
            current_rock = new_rock
      else:
        # print("jet left")
        if not self.rock_side(current_rock, 6):
          new_rock = [r << 1 for r in current_rock]
          if not self.overlap(new_rock, i, tower):
            current_rock = new_rock
      self.draw(tower, i, current_rock)
      if self.overlap(current_rock, i+1, tower):
        # print("Rock falls 1 unit, causing it to come to rest")
        break
      i += 1
      # print("Rock falls 1 unit")
    self.draw(tower, i, current_rock)
    for n, rock_row in enumerate(current_rock):
      pos = i + n
      tower[pos] = tower[pos] | rock_row
    self.draw(tower, i)
    self.t = [row for row in tower if row]
    #print("---")

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
          byte = sum(2 ** i for i, v in enumerate([ch == "#" for ch in l]) if v)
          r.append(byte)
        if not r:
          rock_list.reverse()
          return rock_list
        r.reverse()
        rock_list.append((w, r))

def main(path, max_count):
  global running

  t = Tower(True)
  n=0
  while n <= max_count:
    if running:
      print(n)
      t.drop()
      time.sleep(1)
    # t.draw()
      n += 1
      t.draw(self.t, 0, t.peek_rock())
      running = False

    t.screen.update_idletasks()
    t.screen.update()

  print(f'height: {t.height()}')
  if t.has_graphics:
    t.screen.mainloop()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path, 11)
