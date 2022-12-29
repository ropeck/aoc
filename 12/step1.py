#!/usr/bin/python3
from collections import deque
import os
import sys
import time

class Map:
  MOVES = [(1, 0, 'R'), (0, -1, 'U'), (0, 1, 'D'), (-1, 0, 'L')]

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

  def map_height(self, x, y):
    if not self.in_bounds(x,y):
      return None
    m = self.map[y][x]
    if m == Map.charmap('S'):
      m = 0
    if m == Map.charmap('E'):
      m = 26
    return m

  def in_bounds(self, x, y):
    return not (x < 0 or y < 0 or x > self.width() - 1 or y > self.height() - 1)

  def move_allowed(self, x, y, nx, ny):
    return self.map_height(nx, ny) - self.map_height(x, y) <= 1

  def check_spot_dfs(self, x, y, path=None):
    if not path:
      path = []
    visited = []
    if self.map[y][x] == Map.charmap('E'):
      print('found')
      self.found.append(path)
      return
    print(f'check_spot({x},{y}){self.map[y][x]} {len(path)} {len(self.found)}')
    for (cx, cy) in Map.MOVES:
      if (cx, cy) in visited:
        continue
      nx = x + cx
      ny = y + cy
      if in_bounds(nx, ny) and move_allowed(x, y, nx, ny):
        self.check_spot(x + cx, y + cy, (path + [(nx, ny)]).copy(), (visited + [(nx, ny)]).copy() )


  def draw(self, path):
    os.system('clear')
    m = [l.copy() for l in self.map]
    for (x, y, p) in self.queue:
      m[y][x] = ord(' ')-ord('a')
    for (x, y) in path:
      m[y][x] = ord('*')-ord('a')
    print(path)
    for l in m:
      print ("".join([chr(ord('a') + i) for i in l]))
    time.sleep(0.1)

  def check_spot(self, x, y, path=None, visited=None):
    if not path:
      path = []
    if self.map[y][x] == Map.charmap('E'):
      print('found')
      self.found.append(path+[(x,y)])
      return
    q = []
    for i in self.queue:
      (a,b,p) = i
      q.append((a,b))

    print(f'check_spot({x},{y}){self.map[y][x]} {path} {len(self.queue)} {len(path)} ')
    for (cx, cy, l) in Map.MOVES:
      nx = x + cx
      ny = y + cy
      if (nx, ny) in visited + path:
        continue
      visited.append((nx,ny))
      print(f'  ({nx},{ny}){l} {len(self.queue)}')
      if (self.in_bounds(nx, ny) and
          self.move_allowed(x,y, nx, ny) and
  #            (nx, ny) not in q,
          (nx, ny) not in path):
        print(f'    added')
        self.queue.append((nx, ny, path + [(x, y)], ))

  def find_paths(self):
    self.found = []
    self.queue = deque([self.start() + ([], )])
    visited = []
    while self.queue:
      q = self.queue
      (cx, cy, path) = self.queue.pop()
      self.draw(path)
      self.check_spot(cx, cy, path, visited)
      visited.append((cx, cy))
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
