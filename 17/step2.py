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

  print(f'tower is {len(t)} tall')
  match = None
  stop_loop = False
  for a in range(len(t)):
    if match and a == match[1]:
      print("caught middle")
      break

    for b in range(a+1, len(t)):
      if stop_loop:
        stop_loop = False
        break
      if t[a] == t[b]:
        for i in range(len(t) - b):
          if t[a + i] != t[b + i]:
            break
          if match and a + i > match[1]:
            # print(f'middle overlap: {a} {a+i}')
            stop_loop = True
            break
        if not match or (i > match[2]):
          match = (a, b, i)
          print(match)


  print(match)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)


