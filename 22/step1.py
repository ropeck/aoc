#!/usr/bin/python3
import re
import sys

def main(path):
  map = []
  with open("input","r") as fh:
    while True:
      line = fh.readline().strip()
      if not line:
        break
      map.append(list(line))

    follow = re.findall("(\d+)([LR])",fh.read().strip())
  print(follow)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
