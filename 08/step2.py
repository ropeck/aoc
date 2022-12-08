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
    for i in row:
      if self.sq[y][x] >= i:
        c += 1
      else:
        break
    print (f'  {row} {self.sq[y][x]} {c}')
    return c

  def vis_to_left(self, x, y):
    row = [self.sq[y][i] for i in range(x)]
    row.reverse()

    print("left")
    return self.num_seen(row, x, y)

  def vis_to_right(self, x, y):
    row = [self.sq[y][i] for i in range(x+1, self.width)]
    print("right")
    return self.num_seen(row, x, y)

  def vis_to_top(self, x, y):
    col = [self.sq[i][x] for i in range(y)]
    print("top")
    return self.num_seen(col, x, y)

  def vis_to_bottom(self, x, y):
    col = [self.sq[i][x] for i in range(y+1, self.height)]
    print("bot")
    return self.num_seen(col, x, y)

  def vis(self, x, y):
    return [self.vis_to_left(x, y), self.vis_to_right(x, y), self.vis_to_top(x, y), self.vis_to_bottom(x, y)]

  def count_visible(self):
    total = 0
    for y in range(self.height):
      for x in range(self.width):
        m = 1
        for n in self.vis(x, y):
          m = m * n
        print(f'[{y},{x}] {self.sq[y][x]} {self.vis(x, y)} {m}')
        if self.vis(x, y):
          total += 1
    return total

def main():
  path = sys.argv[1]
  f = Forest(path)
  total = f.count_visible()
  print(f'total visible: {total}')

if __name__ == '__main__':
  main()
