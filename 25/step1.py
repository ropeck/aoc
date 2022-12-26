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

def carry(n, i):
  if i < len(n)-1:
    if str(n[i+1]) in "-=":
      v = "012-=".index(str(n[i+1]))
    else:
      v = int(n[i+1])

    n[i+1] = (v + 1)
    if n[i+1] > 4:
      n[i+1] = n[i+1] % 5
      n = carry(n, i+1)
  else:
    n.append(1)
  return n

def toSnafu(d):
  n = numberToBase(d, 5)
  n1 = n.copy()
  n.reverse()
  for i, v in enumerate(n):
    if v == 4:
      n = carry(n, i)
      n[i] = "-"
    if v == 3:
      n = carry(n, i)
      n[i] = "="
  n.reverse()
  conv = "".join([str(i) for i in n])
  return conv

def fromSnafu(n):
  n = list(n)
  for i, v in enumerate(n):
    if str(v) in "-=":
      n[i-1] = int(n[i-1]) - 1
      if v == "-":
        n[i] = 4
      else:
        n[i] = 3
  conv = sum([(5**(i))*int(n) for i,n in enumerate(n)])
  return conv

def main(path):
  total = 0
  with open(path, "r") as fh:
    line = True
    while line:
      line = fh.readline().strip()
      if not line:
        break
      d = line.split()
      rev = fromSnafu(d[0])
      total += rev
  print(f'total: {total}  {toSnafu(total)}')

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
