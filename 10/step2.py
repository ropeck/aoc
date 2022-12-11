#!/usr/bin/python3
import sys

def debug(str):
  # print(str)
  pass

def main(path):
  t = 0
  carry = None
  reg = 1
  empty_line = [' ' for x in range(40)]
  display = [empty_line.copy() for i in range(6)]
  with open(path, "r") as fh:
    lines = fh.read().splitlines()
  lines.reverse()
  while lines:
    debug(f'{t} {reg} {t * reg}')
    if reg-1 <= t%40 and reg+1 >= t%40:
      display[int(t/40)][t%40] = '#'
    t += 1
    if carry:
      reg += carry
      carry = None
    else:
      line = lines.pop()
      debug(line)
      if line == "noop":
        pass
      else:
        (cmd, val) = line.split()
        if cmd == "addx":
          carry = int(val)
        else:
          print("unknown line " + line)
  for l in display:
    print(''.join(l))
  return display




if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  print(main(path))
