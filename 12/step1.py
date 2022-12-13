#!/usr/bin/python3
import sys
from collections import deque

class Map:
  MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]

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
    try:
      return self.map_height(nx, ny) - self.map_height(x, y) <= 1
    except TypeError:
      return False
  def check_spot_dfs(self, x, y, path=None, visited=None):
    if not path:
      path = []
    if not visited:
      visited = {}

    if self.map[y][x] == Map.charmap('E'):
      print('found')
      self.found.append(path)
      return
    print(f'check_spot({x},{y},{self.map[y][x]} {len(path)}')
    for (cx, cy) in Map.MOVES:
      nx = x + cx
      ny = y + cy
      if visited.get((nx, ny), None):
        continue
      if in_bounds(nx, ny) and move_allowed(x,y, nx, ny):
        visited[(nx, ny)] = 1
        self.check_spot(x + cx, y + cy, path + [(nx, ny)], visited.copy())


  def check_spot(self, x, y, path=None):
    if not path:
      path = []

    if self.map[y][x] == Map.charmap('E'):
      print('found')
      self.found.append(path)
      return
    print(f'check_spot({x},{y},{self.map[y][x]} {len(self.queue)} {len(path)} {len(self.found)}')
    for (cx, cy) in Map.MOVES:
      nx = x + cx
      ny = y + cy
      if all([self.in_bounds(nx, ny),
              self.move_allowed(x,y, nx, ny),
              (nx, ny) not in path]):
        self.queue.append((nx, ny, path + [(nx, ny)]))
    return path

  def find_paths(self):
    self.found = []
    self.queue = deque([self.start() + ([],)])
    while self.queue:
      (cx, cy, path) = self.queue.popleft()
      self.check_spot(cx, cy, path)
    print(self.found)
    return self.found

def main(path):
  map = Map(path)
  map.print()
  found = map.find_paths()
  found.sort(key=lambda p: len(p))
  print(f'shortest path {len(found[0])}')
  print(found[0])
  return len(found[0])

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
