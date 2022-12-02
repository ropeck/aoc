#!/usr/bin/python

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# Rock A/X, Paper B/Y, Scissor C/Z
# score X:1, Y:2, Z:3
#
# A Z

score = {"A": {"X":3, "Y":6, "Z":0},
         "B": {"X":0, "Y":3, "Z":6},
         "C": {"X":6, "Y":0, "Z":3}}

init = {"X": 1, "Y": 2, "Z": 3}


def main():
  total = 0 
  for line in open("input","r"):
    (opp, you) = line.split()
    game = score[opp][you] + init[you]
    print opp, you, game
    total += game
  print("total: ", total)
if __name__ == '__main__':
  main()
