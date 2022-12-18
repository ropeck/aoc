#!/usr/bin/python3
import numpy as np
from pprint import pprint
import sys


def main(path):
  p = []
  with open(path, "r") as fh:
    for l in fh:
      print(l.strip())
      p.append(tuple([int(x) for x in l.strip().split(",")]))
  pprint(p)
  sort(p)
  pprint(p)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
