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
    if (nx, ny) == self.start():
      f = 0
    if (nx, ny) == self.finish():
      f = 26
    # print(f'({x},{y}) -> ({nx},{ny}) = {f-s}')
    return f - s

  def move_allowed(self, x, y, nx, ny):
    return self.move_diff(x, y, nx, ny) <= 1

  def draw(self):
    os.system('clear')
    m = [l.copy() for l in self.map]
    for (x, y, p) in self.queue:
      m[y][x] = ord(' ')-ord('a')
      for (px, py, l) in p:
        m[py][px] = ord('+')-ord('a')
    for l in m:
      print ("".join([chr(ord('a') + i) for i in l]))

  def find_paths(self):
    self.found = []
    self.visited = []
    drawn = 0
    sx, sy = self.start()
    self.queue = deque([(sx, sy, [])])
    while self.queue:
      q = self.queue
      (x, y, path) = self.queue.popleft()
      if (x, y) in self.visited:
        continue
      self.visited.append((x, y))

      if len(path) > drawn:
        self.draw()
        drawn = len(path)



      # print(f'check_spot({x},{y}){self.map[y][x]} {len(self.queue)} {len(path)} ')
      for (cx, cy, l) in Map.MOVES:
        nx = x + cx
        ny = y + cy
        try:
          v = self.map[ny][nx]
        except IndexError:
          v = "OOB"
        # print(f'  ({nx},{ny}){v} {l} {len(self.queue)}')

        if self.in_bounds(nx, ny) and self.move_allowed(x, y, nx, ny):
          if (nx, ny) == self.finish():
            # print('found')
            self.found.append(path + [(x, y, 'F')])
            continue
          self.queue.append((nx, ny, path + [(x, y, l)]))
          # print(f'    added')
    return self.found

def main(path):
  map = Map(path)
  map.print()
  found = map.find_paths()
  found.sort(key=lambda p: len(p))
  print(found[0])
  map.draw(found[0])
  print(f'shortest path {len(found[0])-1}')
  print(f'total found {len(found)}')
  return len(found[0])

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
