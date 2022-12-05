#!/usr/bin/python3
import re

def readstacks(fh):
  lines = []
  max = 0
  while True:
    line = fh.readline().replace("\n","")
    lines.append(line)
    if len(line)>max:
      max = len(line)
    if line == "":
      break
  stack = [" "*len(lines) for n in range(max)]

  for l in lines:
    for i in range(len(l)):
      stack[i] = l[i] + stack[i]

  st = []
  for row in stack:
    if row[0].isnumeric():
      st.append([x for x in row[1:].strip()])
  print(st)
  return st

def main():
  total = 0
  m = re.compile("^move (\d+) from (\d+) to (\d+)$")

  with open("input","r") as fh:
    st = readstacks(fh)

    for line in fh:
      r = m.match(line)
      print(r.group(1,2,3))
      n = int(r.group(1))
      f = int(r.group(2)) - 1
      t = int(r.group(3)) - 1 
      p = st[f][-n:]
      print(p)
      st[f] = st[f][:-n]
      p.reverse()
      st[t] = st[t] + p
      print("")
  print(st)
  print("".join([r[-1] for r in st]))
if __name__ == '__main__':
  main()
