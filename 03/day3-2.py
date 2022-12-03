#!/usr/bin/python

def score(c):
  if c.islower():
    return ord(c) - ord("a") + 1
  return 27 + ord(c) - ord("A")

def main():
  total = 0 
  with open("input", "r") as f:
    while True:
      try:
        r1 = set(f.readline().strip())
        r2 = set(f.readline().strip())
        r3 = set(f.readline().strip())
    
        badge = r1.intersection(r2).intersection(r3).pop()
        sc = score(badge)
        print(badge, sc)
        total += sc
      except:
        break


  print("total: ", total)
if __name__ == '__main__':
  main()
