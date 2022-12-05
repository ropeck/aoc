#!/usr/bin/python3
import re

def readstacks(fh):
  stacks = []
  max = 0
  while True:
    line = fh.readline().replace("\n","")
    if len(line)>max:
      max = len(line)
    if line == "":
      break
    stacks.append(line)
  stacks.reverse()

  # number of stacks
  n = int((max+1)/4);

  st = [[] for x in range(n)]
  for row in stacks[1:]:
    for i in range(0,n):
      ch = row[1+4*i]
      if ch != ' ':
        st[i].append(ch)
  return st

def main():
  total = 0
  m = re.compile("^move (\d+) from (\d+) to (\d+)$")

  with open("input","r") as fh:
    st = readstacks(fh)

    for line in fh:
      print (st) 
      r = m.match(line)
      print(r.group(1,2,3))
      n = int(r.group(1))
      f = int(r.group(2)) - 1
      t = int(r.group(3)) - 1 
      p = st[f][-n:]
      print(p)
      st[f] = st[f][:-n]
      st[t] = st[t] + p
      print("")
  print(st)
  print("".join([r[-1] for r in st]))
if __name__ == '__main__':
  main()
