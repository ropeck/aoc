#!/usr/bin/python

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# Rock A/X, Paper B/Y, Scissor C/Z
# score X:1, Y:2, Z:3
#
# X lose, Y draw, Z win
#
score = {"A": {"A":3, "B":6, "C":0},
         "B": {"A":0, "B":3, "C":6},
         "C": {"A":6, "B":0, "C":3}}

init = {"A": 1, "B": 2, "C": 3}

def st(opp, out):
  if out == "Y":
    return opp
  return {"A": {"X": "C", "Z": "B"},
          "B": {"X": "A", "Z": "C"},
          "C": {"X": "B", "Z": "A"}}[opp][out]

def main():
  total = 0 
  for line in open("input","r"):
    print line
    (opp, out) = line.split()
    you = st(opp, out)
    game = score[opp][you] + init[you]
    print game
    total += game
  print("total: ", total)
if __name__ == '__main__':
  main()
