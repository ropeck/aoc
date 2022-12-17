#!/usr/bin/python3
from pprint import pprint
import re
import sys

class Tower:
  def __init__(self):
    self.t = [["." for x in range(7)] for y in range(4)]
    self.top = 0
    with open(path,"r") as fh:
      self.jet = fh.read()

  def drop(self, r):
    # start at top + 3, then apply jets and move down until stopped
    #
    pass

def read_rocks():
  rock_list = []
  with open("rocks","r") as fh:
    while True:
      r = []
      while True:
        l = fh.readline().strip()
        if not l:
          break
        r.append(l)
      if not r:
        return rock_list
      rock_list.append(r)


def main(path):
  r = read_rocks()
  t = Tower()

  print(r)# 
  print(t.jet)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
