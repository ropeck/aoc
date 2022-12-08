#!/usr/bin/python3
import sys

class Forest:
  def __init__(self, path):
    self.sq = []
    for line in open(path,"r"):
      self.sq.append([int(n) for n in line.strip()])
    self.width = len(self.sq[0])
    self.height = len(self.sq)

  def num_seen(self, row, x, y):
    c = 0
    n = self.sq[y][x]
    for i in row:
      c += 1
      if n > i:
        break
    #print (f'  {row} {self.sq[y][x]} {c}')
    return c

  def vis_to_left(self, x, y):
    row = [self.sq[y][i] for i in range(x)]
    row.reverse()
    print(f'left {row} {y},{x} {self.num_seen(row, x, y)}')

    # print("left")
    return self.num_seen(row, x, y)

  def vis_to_right(self, x, y):
    row = [self.sq[y][i] for i in range(x+1, self.width)]
    print(f'right {row} {y},{x} {self.num_seen(row, x, y)}')
    return self.num_seen(row, x, y)

  def vis_to_top(self, x, y):
    col = [self.sq[i][x] for i in range(y)]
    col.reverse()
    print(f'up {col} {y},{x} {self.num_seen(col, x, y)}')
    return self.num_seen(col, x, y)

  def vis_to_bottom(self, x, y):
    col = [self.sq[i][x] for i in range(y+1, self.height)]
    print(f'down {col} {y},{x} {self.num_seen(col, x, y)}')
    return self.num_seen(col, x, y)

  def vis(self, x, y):
    return [self.vis_to_left(x, y), self.vis_to_right(x, y), self.vis_to_top(x, y), self.vis_to_bottom(x, y)]

  def count_visible(self):
    max = (0, None)
    for y in range(self.height):
      for x in range(self.width):
        print(f'* {y},{x}')
        m = 1
        v = self.vis(x, y)
        for n in v:
          m = m * n
        print(f'[{y},{x}] {self.sq[y][x]} {v} {m}')
        if m > max[0]:
          max = (m, [y, x])
      print("")
    return max

def main():
  path = sys.argv[1]
  f = Forest(path)
  total = f.count_visible()
  print(f'best spot: {total}')

if __name__ == '__main__':
  main()
