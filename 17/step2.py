#!/usr/bin/python3
from icecream import ic
import step1
import sys

def main(path):
  try:
    with open("tower-output.new", "r") as fh:
      t = []
      for l in fh:
        t.append([int(i) for i in l.strip().split()])
  except IOError:
    step1.main(path, 10_000_000)
    with open("tower-output.new", "r") as fh:
      t = []
      for l in fh:
        t.append([int(i) for i in l.strip().split()])
  print(f'tower is {len(t)} tall')
  match = None
  stop_loop = False
  for a in range(len(t)):
    if match and a == match[1]:
      print("caught middle")
      continue

    for b in range(a+1, len(t)):
      if stop_loop:
        stop_loop = False
        break
      if t[a][0] == t[b][0]:
        for i in range(len(t) - b):
          if t[a + i][0] != t[b + i][0]:
            break
          if match and a + i > match[1]:
            # print(f'middle overlap: {a} {a+i}')
            stop_loop = True
            break
        if not match or (i > match[2]):
          match = (a, b, i, t[a + i][1])
          print(match)


  print(match)
  pass
if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)


