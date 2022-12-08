#!/usr/bin/python3
import sys

class Forest:
  def __init__(self, path):
    self.sq = []
    for line in open(path,"r"):
      self.sq.append([int(n) for n in line.strip()])
    self.width = len(self.sq[0])
    self.height = len(self.sq)

  def is_tallest(self, row, x, y):
    if not row:
      return False
    return self.sq[x][y] == max(row)

  def vis_from_left(self, x, y):
    row = [self.sq[i][y] for i in range(x)]
    return self.is_tallest(row, x, y)


  def vis_from_right(self, x, y):
    row = [self.sq[i][y] for i in range(x-1, self.width)]
    return self.is_tallest(row, x, y)

  def vis_from_top(self, x, y):
    col = [self.sq[x][i] for i in range(y)]
    return self.is_tallest(col, x, y)

  def vis_from_bottom(self, x, y):
    col = [self.sq[x][i] for i in range(y-1, self.height)]
    return self.is_tallest(col, x, y)

  def vis(self, x, y):
    return any([self.vis_from_left(x, y), self.vis_from_right(x, y), self.vis_from_top(x, y), self.vis_from_bottom(x, y)])

  def count_visible(self):
    total = 0
    for y in range(self.height):
      for x in range(self.width):
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
