#!/usr/bin/python3
import aocd
import re
import sys

def main(test):
  total = 0
#  test = 1
  mod = aocd.models.Puzzle(year=2023, day=4)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
    pass

  line = 1
  off = {}
  for card in data.splitlines():
    print(card)
    m = re.match(r"Card.*:([ \d]+) \|(.*)", card)
    if not m:
      print("no match?", card)
      sys.exit(1)
    win_str, card_str = m.groups()
    score = 0
    winners = [int(x) for x in win_str.split()]
    for card in [int(x) for x in card_str.split()]:
      if card in winners:
        score += 1
        off[score+line] = off.get(score+line, 0) + (1 + off.get(line, 0))
  #      print("win", score, off[score+line], card)


    line += 1

  print(off)
  print(total)
  total = sum(off.values()) + line - 1
  print("sum", total)
  if not test:
      aocd.submit(total, part="b", day=4, year=2023)


if __name__ == '__main__':
  main(len(sys.argv) > 1)
