#!/usr/bin/python3
from icecream import ic
import step1
import sys

def main(path):
  try:
    with open("tower-output.new", "r") as fh:
      t = [int(l.strip()) for l in fh]
  except:
    step1.main(path, 10_000_000)
    with open("tower-output.new", "r") as fh:
      t = [int(l.strip()) for l in fh]

  match = None
  for a in range(len(t)):
    for b in range(a+1, len(t)):
      if t[a] == t[b]:
        for i in range(len(t) - b):
          if t[a + i] != t[b + i]:
            break
        if not match or (i > match[2]):
          match = (a, b, i)


  print(match)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)


