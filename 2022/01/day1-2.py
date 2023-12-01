#!/usr/bin/python
def main():
  elf = []
  total = 0
  for line in open("input","r"):
    if line.strip() == "":
      elf.append(total)
      total = 0
    else:
      total += int(line.strip())
  elf.sort()
  print sum(elf[-3:])

if __name__ == '__main__':
  main()
