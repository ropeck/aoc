#!/usr/bin/python3
import aocd
from collections import deque
import os
import sys

class Map:
  MOVES = [(0, -1, 'U'), (0, 1, 'D'), (1, 0, 'R'), (-1, 0, 'L')]
  START = ord('S') - ord('a')
  FINISH = ord('E') - ord('a')

  def charmap(char):
    return ord(char) - ord('a')

  def __init__(self, data):
    m = []
    for l in data.splitlines():
      m.append([ord(i)-ord('a') for i in l.strip()])
    self.map = m
    self.char_cache = {}

  def print(self):
    for l in self.map:
      print(l)
    for o in "start finish width height".split():
      print(f'{o}: {eval("self."+o+"()")}')

  def find_char(self, char):
    r = self.char_cache.get(char, None)
    if r:
      return r
    y = 0
    for l in self.map:
      x = 0
      for i in l:
        if self.map[y][x] == Map.charmap(char):
          r = (x, y)
          break
        x += 1
      if r:
        break
      y += 1
    self.char_cache[char] = r
    return r

  def start(self):
    return self.find_char('S')

  def finish(self):
    return self.find_char('E')

  def width(self):
    return len(self.map[0])

  def height(self):
    return len(self.map)

  def in_bounds(self, x, y):
    return not (x < 0 or y < 0 or x > self.width() - 1 or y > self.height() - 1)

  def move_diff(self, x, y, nx, ny):
    s = self.map[y][x]
    f = self.map[ny][nx]
    if (x, y) == self.start():
      s = 0
    if (x, y) == self.finish():
      s = 25
    if (nx, ny) == self.start():
      f = 0
    if (nx, ny) == self.finish():
      f = 25
    # print(f'({x},{y}) -> ({nx},{ny}) = {f-s}')
    return f - s

  def move_allowed(self, x, y, nx, ny):
    return self.move_diff(nx, ny, x, y) <= 1  # backwards going down

  def draw(self, path=None):
    os.system('clear')
    m = [l.copy() for l in self.map]
    if path:
      for (px, py, l) in path:
        m[py][px] = ord('*') - ord('a')
    for (x, y, p) in self.queue:
      m[y][x] = ord(' ')-ord('a')
      for (px, py, l) in p:
        m[py][px] = ord('+')-ord('a')
    for l in m:
      print ("".join([chr(ord('a') + i) for i in l]))
    print("")

  #@pysnooper.snoop()
  def find_paths(self):
    self.found = []
    self.visited = []
    drawn = 0
    sx, sy = self.finish()
    self.queue = deque([(sx, sy, [])])
    while self.queue:
      q = self.queue
      (x, y, path) = self.queue.popleft()

      if len(path) > drawn:
        self.draw()
        drawn = len(path)

      for (cx, cy, l) in Map.MOVES:
        nx = x + cx
        ny = y + cy
        if (nx, ny) in self.visited + [(x,y) for (x,y,_) in list(self.queue)]:
          continue
        if self.in_bounds(nx, ny) and self.move_allowed(x, y, nx, ny):
          if nx == 0:
            self.found.append(path + [(x, y, 'F')])
            continue
          self.queue.append((nx, ny, path + [(x, y, l)]))
          self.visited.append((nx, ny))
    return self.found


def main(test=False):
  m = aocd.models.Puzzle(year=2022, day=12)
  if test:
    data = m.example_data
  else:
    data = m.input_data
  map = Map(data)
  map.print()
  found = map.find_paths()
  found.sort(key=lambda p: len(p))
  print(found[0])
  map.draw(found[0])
  print(f'shortest path {len(found[0])}')
  print(f'total found {len(found)}')
  return len(found[0])

if __name__ == '__main__':
  main(len(sys.argv) > 1)
