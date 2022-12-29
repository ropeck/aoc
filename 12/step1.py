#!/usr/bin/python3
from collections import deque
import os
import random
import sys
import time

class Map:
  MOVES = [(0, -1, 'U'), (0, 1, 'D'), (1, 0, 'R'), (-1, 0, 'L')]
  START = ord('S') - ord('a')
  FINISH = ord('E') - ord('a')

  def charmap(char):
    return ord(char) - ord('a')

  def __init__(self, path):
    m = []
    with open(path, "r") as fh:
      for l in fh:
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
    if (nx, ny) == self.s
      tart():
      f = 0
    if (nx, ny) == self.finish():
      f = Map.charmap(FINISH)
    print(f'({x},{y}) -> ({nx},{ny}) = {f}')
    return f - s

  def move_allowed(self, x, y, nx, ny):
    return self.move_diff(x, y, nx, ny) <= 1

  def draw(self, path):
    os.system('clear')
    m = [l.copy() for l in self.map]
    for (x, y, p) in self.queue:
      m[y][x] = ord(' ')-ord('a')
    for (x, y) in path:
      m[y][x] = ord('*')-ord('a')
    # print(path)
    for l in m:
      print ("".join([chr(ord('a') + i) for i in l]))

  def check_spot(self, x, y, path=None):
    if not path:
      path = []
    self.visited.append((x, y))
    visited = self.visited
    if self.map[y][x] == Map.charmap('E'):
      print('found')
      self.found.append(path+[(x,y)])
      return

    print(f'check_spot({x},{y}){self.map[y][x]} {len(self.queue)} {len(path)} ')
    random.shuffle(Map.MOVES)
    for (cx, cy, l) in Map.MOVES:
      nx = x + cx
      ny = y + cy
      print(f'  ({nx},{ny}){l} {len(self.queue)}')
      if (self.in_bounds(nx, ny) and
          self.move_allowed(x,y, nx, ny) and
          (nx, ny) not in visited + path):
        print(f'    added')
        self.queue.append((nx, ny, path + [(x, y)]))

  def find_paths(self):
    self.found = []
    self.visited = []
    sx, sy = self.start()
    self.queue = deque([(sx, sy, [])])
    while self.queue:
      q = self.queue
      (cx, cy, path) = self.queue.popleft()
      self.draw(path)
      self.check_spot(cx, cy, path)
      print('')
      if self.found:
        break
  #  print(self.found)
    return self.found

def main(path):
  map = Map(path)
  map.print()
  found = map.find_paths()
  found.sort(key=lambda p: len(p))
  print(found[0])
  print(f'shortest path {len(found[0])}')
  print(f'total found {len(found)}')
  map.draw(found[0])
  return len(found[0])

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
