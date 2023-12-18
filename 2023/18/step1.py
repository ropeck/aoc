#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 18

class Lagoon:
  def __init__(self, data):
    self.steps = data
    x = 0
    y = 0
    orig_x = x
    orig_y = y
    self.width = 0
    self.height = 0
    for line in data:
      dir, lenstr, color = line.split(" ")
      n = int(lenstr)
      if dir == "R":
        x += n
      if dir == "L":
        x -= n
      if dir == "D":
        y -= n
      if dir == "U":
        y += n
      if x < 0:
        self.width -= x
        orig_x -= x
        x = 0
      self.width = max([self.width, x])
      if y < 0:
        self.height -= y
        orig_y -= y
        y = 0
      self.height = max([self.height, y])

    if x < 0 or y < 0:
      raise ValueError

    self.d = [["." for x in range(self.width+1)]
              for y in range(self.height+1)]

    x = orig_x
    y = orig_y
    for line in data:
      dir, lenstr, color = line.split(" ")
      n = int(lenstr)
      while n:
        if dir == "R":
          x += 1
        if dir == "L":
          x -= 1
        if dir == "D":
          y -= 1
        if dir == "U":
          y += 1
        self.d[y][x] = "#"
      #  self.draw()
      #  print("")
        n -= 1
  def draw(self, data=None):
    if not data:
      data = self.d
    for line in data:
      print("".join(line))

  def count(self):
    # make a border around the data
    frame = [["." for i in range(len(self.d[0])+2)]]
    mid = [["."] + line + ["."] for line in self.d]
    box = frame + mid + frame
    print (f"{len(box[0])}x{len(box)}")
    self.draw(box)
    # fill from the edge
    x = 0
    y = 0
    q = [(x,y)]
    s = {}
    while q:
      cur = q.pop(0)
      x, y = cur
      # print(cur, q)
      s[cur] = True
      box[y][x] = " "
      for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if ((nx < 0 or nx > self.width + 2) or
            (ny < 0 or ny > self.height + 2)):
            continue
        if (nx, ny) in s:
          continue
        if box[ny][nx] != "#" and (nx, ny) not in q:
          s[(nx, ny)] = True # this may be quicker
          q.append((nx, ny))
    # count the spaces not filled
    total = (self.width + 3) * (self.height + 3) - len(s)
    self.draw(box)
    return total


def main(test):
  #test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  lag = Lagoon(data)
  #lag.draw()
  total = lag.count()
  print("total", total)
  if not test:
    aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
