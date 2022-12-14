#!/usr/bin/python3
import sys

class Drawing:
  def __init__(self, path):
    drawing = []
    with open(path,"r") as fh:
      for line in fh:
        drawing.append([tuple(p.split(",")) for p in line.strip().split(" -> ")])
    print(drawing)
    self.d = drawing

def main(path):
  d = Drawing(path)
  return d.d

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
