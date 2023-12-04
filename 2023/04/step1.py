#!/usr/bin/python3
import aocd
import re
import sys

def main(test):
  total = 0
  #test = 1
  mod = aocd.models.Puzzle(year=2023, day=4)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
    pass

  for card in data.splitlines():
    m = re.match(r"Card.*:([ \d]+) \|(.*)", card)
    if not m:
      print("no match?", card)
      sys.exit(1)
    win_str, card_str = m.groups()
    score = 0
    winners = [int(x) for x in win_str.split()]
    for card in [int(x) for x in card_str.split()]:
      if card not in winners:
          continue
      if score:
        score = score * 2
      else:
        score = 1
    total += score

  print(total)
  if not test:
      aocd.submit(total, part="a", day=4, year=2023)


if __name__ == '__main__':
  main(len(sys.argv) > 1)
