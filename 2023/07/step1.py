#!/usr/bin/python3
import aocd
import re
import sys
from functools import cmp_to_key

_DAY = 7
CARD_ORDER = '23456789TJQKA'

def card_score(n):
  return CARD_ORDER.index(n)

class Hand:
  def __init__(self, line):
    self.str = line
    self.cards = {}
    (card_str, bid_str) = line.split(" ")
    self.bid = int(bid_str)
    for c in card_str:
      self.cards[c] = self.cards.get(c, 0) + 1
    
    self.hand = sorted(self.cards.items(),
                       key=lambda n: n[1]*100+card_score(n[0]),
                       reverse=True)

  def pairs(self):
    return self.hand[0][1]
  
  def __lt__(self, other):
    return self.cmp(other) < 0
  def __gt__(self, other):
    return self.cmp(other) > 0
  def __eq__(self, other):
    return self.cmd(other) == 0
  def __repr__(self):
    return f"Hand({self.str})"
  def cmp(self, other):
    sp = self.pairs()
    op = other.pairs()
    if sp < op:
      return -1
    if sp > op:
      return 1
    ss = card_score(self.hand[0][0])
    os = card_score(other.hand[0][0])
    if ss < os:
      return -1
    if ss > os:
      return 1
    # same pairs, same values
    if sp == 4:
      ss = card_score(self.hand[1][0])
      os = card_score(other.hard[1][0])
      if ss < os:
        return -1
      if ss > os:
        return 1
      # same second pair values?
      return 0
    
  # Every hand is exactly one type. From strongest to weakest, they are:

  # 7 Five of a kind, where all five cards have the same label: AAAAA
  # 6 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
  # 5 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
  # 4 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
  # 3 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
  # 2 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4   
  # 1 High card, where all cards' labels are distinct: 23456



def main(test):
  total = 0
  test = 1

  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  hands = []
  for line in data:
    hands.append(Hand(line))
  hands = sorted(hands, reverse=True)

  if not test:
      aocd.submit(ans, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
