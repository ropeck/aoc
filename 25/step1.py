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
      v = int(i)

    n[i+1] = (v + 1)
    if n[i+1] > 4:
      n[i+1] = n[i+1] % 5
      n = carry(n, i+1)
  else:
    n.append(1)
  return n

def borrow(n, i):
  if i < len(n):
    v = "012=-".index(str(n[i]))
    if v == 0:
      #n = borrow(n, i+1)
      n[i] = 4
    if v == 3:
      n = borrow(n, i+1)
      n[i] = 2
    else:
      n[i] = v - 1
  return n

def toSnafu(d):
  n = numberToBase(d, 5)
  n1 = n.copy()
  n.reverse()
  for i, v in enumerate(n):
    if v == 4:
      if i < len(n)-1:
        n = carry(n, i)
      else:
        n.append(1)
      n[i] = "-"
    if v == 3:
      if i < len(n)-1:
        n = carry(n, i)
      else:
        n.append(1)
      n[i] = "="
  n.reverse()
  print("toSnafu",d, n1, n)
  conv = "".join([str(i) for i in n])
  return conv

def fromSnafu(n):
  print("from Snafu", n)
  n = list(n)
  n.reverse()
  for i, v in enumerate(n):
    print(i,v)
    if str(v) in "-=":
      n = borrow(n, i+1)
      if n[i] == "-":
        n[i] = 4
      else:
        n[i] = 3
  # n.reverse()
  conv = sum([(5**(i))*int(n) for i,n in enumerate(n)])
  r = n.copy()
  r.reverse()
  return r, conv

def main(path):
  total = 0
  mismatch = []

  with open(path, "r") as fh:
    header = fh.readline()
    line = True
    while line:
      line = fh.readline().strip()
      if not line:
        break
      d = line.split()
      conv = toSnafu(int(d[1]))
      rev = fromSnafu(d[0])
      print (line, conv, rev)
      if (int(d[1]) != rev[-1]):
        print("MISMATCH")
        mismatch.append(str((d, conv, rev)))
      print("")

  #print(f'total: {total}')
  if mismatch:
    print("MISMATCH TOTAL")
    print("\n".join(mismatch))
  else:
    print("no mismatched")

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
