#!/usr/bin/python3
import sys

def main(path):
  total = 0
  # with open(path, "r") as fh:
  #   line = fh.readline().strip()
  #   while True:

  for line in open(path,"r"):
    pass
  print(f'total: {total}')

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
