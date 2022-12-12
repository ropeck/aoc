#!/usr/bin/python3
import sys

class Map:
  m = []
  for y in [-1, 0, 1]:
    for x in [-1, 0, 1]:
      if x == 0 and y == 0:
        continue
      m.append((x,y))
  MOVES = m

  def __init__(self, path):
    m = []
    with open(path, "r") as fh:
      for l in fh:
        m.append([ord(i)-ord('a') for i in l.strip()])
    self.map = m
    self.char_cache = {}
    self.visited = []

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
        if self.map[y][x] == ord(char)-ord('a'):
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


  def check_spot(self, x, y, path):
    if x < 0 or y < 0 or x > self.width() or y > self.height():
      return
    if (x, y) in self.visited:
      return
    print(f'check_spot({x},{y},{path}')
    if (x, y) not in self.visited:
      self.visited.append((x, y))
    (ex, ey) = self.finish()
    for (cx, cy) in Map.MOVES:
      if cx + x == ex and cy + y == ey:
        print('found')
        self.found.append(path)
        return
      self.check_spot(x + cx, y + cy, path + [(x, y)])

  def find_paths(self):
    self.found = []
    (cx, cy) = self.start()
    self.check_spot(cx, cy, [])
    print(self.found)

def main(path):
  map = Map(path)
  map.print()
  map.find_paths()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
