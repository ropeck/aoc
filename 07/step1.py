#!/usr/bin/python3
import re

class Entry:
  def __init__(self, name, size, parent):
    self.name = name
    self.byte_size = int(size)
    self.parent = parent

  def size(self):
    return self.byte_size

  def __repr__(self):
    return f'{self.name} (file, size={self.size})'

class Dir:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.entries = {}

  def size(self):
    return sum([x.size() for x in self.entries.values()])

  def append(self, entry):
    self.entries[entry.name]=entry

  def __repr__(self):
    return f'{self.name} (dir)'

def print_size(e, indent=0):
  print(f'{indent*"  "}- {e}')
  root = Dir("/", None)
  if type(e) != type(root):
    print ("file")
  if type(e) == type(root):
    for f in e.entries.values():
      print_size(f, indent+1)

def main():
  cwd = None
  line = ""
  root = cwd
  with open("otherinput","r") as fh:
    line = fh.readline().strip()
    while True:
      if line and line[0] != "$":
        line = fh.readline().strip()
      if line == "":
        break
      m = re.match("^\$ cd (.*)", line)
      if m:
        if m.group(1) == "..":
          cwd = cwd.parent
        elif m.group(1) == "/":
          root = Dir("/", None)
          cwd = root
        else:
          cwd = cwd.entries[m.group(1)]
        line = "next"
        continue
      if line == "$ ls":
        while True:
          line = fh.readline().strip()
          if line == "" or line[0] == "$":
            break
          (a, b) = line.split()
          if a == "dir":
            e = Dir(b, cwd)
          else:
            e = Entry(b, a, cwd)
          cwd.append(e)
        continue
      line = fh.readline().strip()

  print(f'{root.size()}')

  print_size(root)

if __name__ == '__main__':
  main()
