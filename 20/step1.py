#!/usr/bin/python3
import sys

def main(path):
  d = []
  with open(path, "r") as fh:
    for line in fh:
      d.append(int(fh.readline()))

  print(d)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
