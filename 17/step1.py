#!/usr/bin/python3
import aocd.models
from aocd import get_data
from collections import deque
from icecream import ic
import sys
import time
import tkinter

running = False

def keypress(event):
  global running

  running = True


def rock_generator(path):
  rocks = read_rocks(path)
  pending_rocks = None
  while True:
    if not pending_rocks:
      pending_rocks = [(n, r.copy()) for n, r in rocks]
    r = pending_rocks.pop()
    yield r


def read_rocks(path):
  rock_list = []
  with open(path, "r") as fh:
    while True:
      r = []
      while True:
        l = fh.readline().strip()
        if not l:
          break
        w = len(l)
        byte = sum(2 ** (w-i-1) for i, v in enumerate([ch == "#" for ch in l]) if v)
        r.append(byte)
      if not r:
        rock_list.reverse()
        return rock_list
      rock_list.append((w, r))


def jet_generator(jet_data):
  jet_data = list(jet_data.strip())
  jet_data.reverse()
  jet = None
  while True:
    if not jet:
      jet = jet_data.copy()
    yield jet.pop()


def overlap(rock, i, tower):
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


def rock_side(r, i):
  for row in r:
    if row & 2**i:
      return True
  return False

def state(jet, tower):
  return jet + "".join([hex(i)[2:] for i in list(tower)[:40]])

class Diagram:
  def __init__(self, has_graphics):
    self.screen = None
    self.border = 15
    self.dx = self.dy = 10
    if has_graphics:
      self.screen = tkinter.Tk()
      self.screen.geometry("200x1200")
      self.canvas = tkinter.Canvas(self.screen, width=100, height=1150)
      self.screen.bind("<space>", keypress)
      self.canvas.pack()
      self.screen.update_idletasks()
      self.screen.update()

  def draw(self, t=None, i=None, r=None):
    if not t:
      t = self.t
    # draw the top 10 rows of the tower.
    # indicate the bottom and next rock position
    n = min([len(t), 100])
    h = n * self.dy + self.border*2
    w = self.border * 2 + 7 * self.dy
    if self.screen:
      c = self.canvas
      b = self.border
      dx = self.dx
      dy = self.dy
      c.create_rectangle(0, 0, 100, 1150, fill="white")
      c.create_rectangle(b, h - b - (n * dy), w - b, h - b, outline="black", fill="light gray")

    for row_num, row in list(enumerate(t)):
      if row == 255:
        continue
      self.draw_row(row, row_num, "blue")
    if r and self.has_graphics():
      ic(i, r)
      for j, rock_row in enumerate(r):
        self.draw_row(rock_row, j + i, "green")
    if self.has_graphics():
      c.create_rectangle(b, h - b - (n * dy), w - b, h - b,
                                     outline="black", fill=None)
      self.screen.update_idletasks()
      self.screen.update()

  def draw_row(self, row, row_num, color):
    for nn in range(6, -1, -1):
      if row & 2 ** nn:
        self.draw_square(6-nn, row_num, color)

  def draw_square(self, nn, row_num, color):
    b = self.border
    dx = self.dx
    dy = self.dy
    x = b + dx * nn
    y = b + dy * row_num
    if self.has_graphics():
      self.canvas.create_rectangle(x, y, x + dx, y + dy, outline="black", fill=color)

  def has_graphics(self):
    return self.screen

  def sleep(self, t):
    return
    if self.screen:
      time.sleep(t)

  def update(self):
    if self.screen:
      self.screen.update_idletasks()
      self.screen.update()

  def mainloop(self):
    if self.screen:
      self.screen.mainloop()


class Tower:
  def __init__(self, jet_data, has_graphics=True):
    self.t = deque()  # each row is a byte
    self.rocknum = deque()
    self.rocks = rock_generator("rocks")
    self.history = {}
    self.jet = jet_generator(jet_data)
    self.height_offset = 0
    self.diagram = Diagram(has_graphics)

  def has_graphics(self):
    return self.diagram.has_graphics()

  def height(self):
    return len(self.t) + self.height_offset

  def drop(self, rnum):
    # start at top + 3, then apply jets and move down until stopped
    # self.t + [0, 0, 0]
    # loop from top down, check to see if the rock overlaps
    # use binary AND of the tower with the rock - if (rock & tower top ) != 0 then it's colliding
    l, m = next(self.rocks)
    r = (l, m)
    rock = r[1].copy()
    current_rock = [row << (5 - r[0]) for row in rock]
    tower = self.t
    padding = [0 for i in current_rock] + [0, 0, 0]
    tower.extendleft(padding)
    self.rocknum.extendleft([[] for i in range(len(padding))])
    i = 0
    while True:
      self.diagram.sleep(1)
      if i + len(current_rock) > len(tower):
        break
      self.diagram.draw(tower, i, current_rock)
      jetdir = next(self.jet)
      if jetdir == ">":
        # print("jet right")
        if not rock_side(current_rock, 0):
          new_rock = [r >> 1 for r in current_rock]
          if not overlap(new_rock, i, tower):
            current_rock = new_rock
      else:
        # print("jet left")
        if not rock_side(current_rock, 6):
          new_rock = [r << 1 for r in current_rock]
          if not overlap(new_rock, i, tower):
            current_rock = new_rock
      self.diagram.draw(tower, i, current_rock)
      if overlap(current_rock, i+1, tower):
        break
      i += 1
      # print("Rock falls 1 unit")
    self.diagram.draw(tower, i, current_rock)
    for n, rock_row in enumerate(current_rock):
      pos = i + n
      tower[pos] = tower[pos] | rock_row
      while len(self.rocknum) < pos+1:
        self.rocknum.append([])
      self.rocknum[pos].append(rnum)
    self.diagram.draw(tower, i)

    while tower[0] == 0:
      tower.popleft()
    while self.rocknum[0] == []:
      self.rocknum.popleft()

    # save the state
    # print("Rock falls 1 unit, causing it to come to rest")
    st = state(jetdir, tower)
    r = self.history.get(st, [])
    r.append((rnum, self.height()))
    self.history[st] = r

    if len(tower) > 50:
      self.height_offset += 1
      tower.pop()
      self.rocknum.pop()
    self.t = tower

  def compute_repeat(self):
    # compute the repeat length and offset from the history
    hist = self.history
    (self.roff, self.hoff), (self.rrep, self.hrep) = [hist[x] for x in hist if len(hist[x]) > 1][0][:2]
    self.rocklen = self.rrep - self.roff
    self.hlen = self.hrep - self.hoff

def main(is_test, max_count):
  global running

  m = aocd.models.Puzzle(year=2022, day=17)
  if is_test:
    # example data shows rock shapes, not the test input, so just use this hardcoded from the instructions
    data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
  else:
    data = m.input_data
  t = Tower(data, False)
  n=1
  while n <= max_count:
    if running or not t.has_graphics():
      print(n)
      t.drop(n)
      t.diagram.sleep(1)
    # t.diagram.draw()
      n += 1
      running = False
    t.diagram.update()

  print(f'height: {t.height()}')

  t.diagram.mainloop()
  t.compute_repeat()
  return t

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = None
  main(path, 2022)
