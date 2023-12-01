#!/usr/bin/python

def score(c):
  if c.islower():
    return ord(c) - ord("a") + 1
  return 27 + ord(c) - ord("A")

def main():
  total = 0 
  for line in open("input","r"):
    line = line.strip()
    r1 = set(line[0:len(line)/2])
    r2 = set(line[len(line)/2:])
    letter = r1.intersection(r2).pop()
    sc = score(letter)
    print(letter, sc)
    total += sc


  print("total: ", total)
if __name__ == '__main__':
  main()
