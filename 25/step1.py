#!/usr/bin/python3
import sys
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def main(path):
  total = 0
  with open(path, "r") as fh:
    header = fh.readline()
    line = True
    while line:
      line = fh.readline().strip()
      d = line.split()
      print(d)
      n = numberToBase(int(d[1]), 5)
      print(n)
      n.reverse()
      for i, v in enumerate(n):
        if v == 4:
          if i < len(n)-1:
            n[i] += 1
          else:
            n.append(1)
          n[i] = "-"
        if v == 3:
          if i < len(n)-1:
            n[i] += 1
          else:
            n.append(1)
          n[i] = "="
      n.reverse()
      print("".join([str(i) for i in n]))
      print("")

  #print(f'total: {total}')

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
