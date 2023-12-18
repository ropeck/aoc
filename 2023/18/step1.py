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
    self.width = 0
    self.height = 0
    for line in data:
      dir, lenstr, color = line.split(" ")
      n = int(lenstr)
      if dir == "R":
        x += n
      if dir == "L":
        x -= n
      if dir == "U":
        y -= n
      if dir == "D":
        y += n
      self.width = max([self.width, x])
      self.height = max([self.height, y])

    self.d = [["." for x in range(self.width+1)] 
              for y in range(self.height+1)]
    
    x = 0
    y = 0
    for line in data:
      dir, lenstr, color = line.split(" ")
      n = int(lenstr)
      while n:
        if dir == "R":
          x += 1
        if dir == "L":
          x -= 1
        if dir == "U":
          y -= 1
        if dir == "D":
          y += 1
        self.d[y][x] = "#"
        n -= 1
  def draw(self):
    for line in self.d:
      print("".join(line))

  def count(self):
    total = 0
    for yd in self.d:
      t = 0
      y = ''.join(yd)
      inside = False
      w = 0
      prev = None
      edge = False
      for x, c in enumerate(yd):
        if c == "#" and prev != "#" and (not edge or (x < len(yd)-1 and yd[x+1] != "#")):
          if c == "#":
            edge = True
          inside = not inside
          if not inside:
            t += 1
        if inside:
          t += 1
        prev = c
      print(y, t)
      total += t
    return total
          

def main(test):
  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  lag = Lagoon(data)
  lag.draw()
  total = lag.count()
  print("total", total)
  if not test:
      aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
