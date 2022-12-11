#!/usr/bin/python3
import sys

def debug(str):
  # print(str)
  pass

def main(path):
  t = 0
  carry = None
  reg = 1
  checkpoint = []
  with open(path, "r") as fh:
    lines = fh.read().splitlines()
  lines.reverse()
  while lines:
    t += 1
    debug(f'{t} {reg} {t * reg}')
    if t == 20 or ((t-20)%40 == 0):
      sig = t * reg
      checkpoint.append(sig)
      debug("checkpoint")
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
  return sum(checkpoint)




if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  print(main(path))
