#!/usr/bin/python3
import aocd
import re
import sys
from containers import Counter

_DAY = 7
  # Every hand is exactly one type. From strongest to weakest, they are:

  # 7 Five of a kind, where all five cards have the same label: AAAAA
  # 6 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
  # 5 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
  # 4 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
  # 3 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
  # 2 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
  # 1 High card, where all cards' labels are distinct: 23456

CARD_ORDER = '23456789TJQKA'
_FIVE_OF = 7
_FOUR_OF = 6
_FULL_HOUSE = 5
_THREE_OF = 4
_TWO_PAIR = 3
_TWO_OF = 2
_ONE_OF = 1

def hand_score(hc)
  h = sorted(hc.items(), key=lambda i: i[1], reverse=True)
  if len(h) == 1:
    return _FIVE_OF
  if len(h) == 2:
    if h[0][1] == 4:
      return _FOUR_OF
    return _FULL_HOUSE
  if len(h) == 3:
    if h[0][1] == 3:
      return _THREE_OF
    return _TWO_PAIR
  if len(h) == 4:
    return _TWO_OF
  return _ONE_OF

def card_cmp(a,b):
  sa = card_score(a[0])
  sb = card_score(b[0])
  if sa < sb:
    return -1
  if sa > sb:
    return 1
  return 0

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

  def pairs(self, n=0):
    return self.hand[n][1]
  
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
    s = card_cmp(self.hand[0], other.hand[0])
    if s:
      return s
    # same pairs, same values
    if sp == 4:
      return card_cmp(self.hand[1], other.hand[1])
    if sp == 3:
      sp = self.pairs(1)
      op = other.pairs(1)
      if sp < op:
        return -1
      if sp > op:
        return 1
      return card_cmp(self.hand[1], other.hand[1])

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
  hands = sorted(hands, reverse=True)

  if not test:
      aocd.submit(ans, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
