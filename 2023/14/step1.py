#!/usr/bin/python3
import aocd
import re
import snoop
import sys


_DAY = 14

def print_board(b):
  print("\n".join([i.decode() for i in b]))

ROUND = ord("O")
CUBE = ord("#")
EMPTY = ord(".")

def main(test):
  #test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  b = [bytearray(line, "utf-8") for line in data]

  print_board(b)
  print("---")

  total = 0
  for y, row in enumerate(b):
    if y == 0:
        continue
    for x, v in enumerate(row):
      if v == ROUND:
        yy = y
        ny = yy - 1
        while b[ny][x] == EMPTY and ny >= 0:
          b[yy][x] = EMPTY
          b[ny][x] = ROUND
          ny -= 1
          yy -= 1
  print_board(b)
  print("---")
  for y, row in enumerate(b):
    for x, v in enumerate(row):
      if v == ROUND:
        total+= len(b)-y

  print("total", total)
  if not test:
    aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
