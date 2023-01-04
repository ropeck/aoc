#!/usr/bin/python3
import os
#import snoop
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
      self.screen.geometry("1200x1250")
      self.canvas = tkinter.Canvas(self.screen, width=70 * 5, height=220 * 5)
      # self.canvas.create_rectangle(gx, gy, gx + self.width * 5, gy + self.height * 5,
      #                              outline="black", fill="light gray")
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
    return


    if not t:
      t=self.t
   # print(f'{r} {i} {t}')
    row_num = 0
    for row in t:
      if row == 255:
        continue
      s=""
      for n in range(7):
        nn = 6-n
        m=2**nn
        if (r and (row_num>=i) and (row_num<=i+len(r)-1) and m & r[row_num-i]):
          s += "@"
        elif (m & row):
          s += "#"
        else:
          s += "."
      print(f'|{s}|')
      row_num += 1
    print('+-------+')
    print('')

  def overlap(self, rock, i, tower):
  #   for n, rock_row in enumerate(new_rock):
  #     if tower[i-n] & rock_row:
  #       return True
  #   return False
  # #
    for j, rr in enumerate(rock):
      tr = i + j
      # print(f'overlap tr={tr} len(rock)={len(rock)} i={i}')
      if tr > len(tower) - 1:
        return True
      o = tower[tr] & rock[j]
      # print(f'o:{o} tower[tr] {tower[tr]} tr {tr}  rock[j] {rock[j]}  j {j}')
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
    # print(list(enumerate(tower)))
    # self.draw_rock(current_rock)
    place = 0
    i = 0 
    while True:
      if i > len(tower)+1:
        break
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
    # print(f'i={i} place={place} pos={1+i-len(current_rock)}')
    for n, rock_row in enumerate(current_rock):
      pos = i + n
      tower[pos] = tower[pos] | rock_row
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
