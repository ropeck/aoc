#!/usr/bin/python3
import re

class Entry:
  def __init__(self, name, size, parent):
    self.name = name
    self.byte_size = int(size)
    self.parent = parent

  def size(self):
    return self.byte_size

  def __str__(self):
    return f'{self.name} (file, size={self.size()})'
  def isDir(self):
    return False

class Dir:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.entries = {}

  def path(self):
    if self.parent:
      return f'{self.parent.path()}/{self.name}'
    else:
      return ""

  def isDir(self):
    return True

  def size(self):
    return sum([x.size() for x in self.entries.values()])

  def append(self, entry):
    self.entries[entry.name]=entry

  def __str__(self):
    return f'{self.name} (dir)'

def print_size(e, indent=0):
#  print(f'ps {e.name} {type(e)} {type(Dir("", None))}')
  print(f'{indent*"  "}- {e}')
  root = Dir("/", None)
  if type(e) == type(root):
    for f in e.entries.values():
      print_size(f, indent+1)


def find_big_directories(e):
  global collected
  if e.isDir():
    print(f'{e.path()} {e.size()}')
    collected.append(e)
  root = Dir("/", None)
  if type(e) == type(root):
    for f in e.entries.values():
      find_big_directories(f)

def main():
  cwd = None
  line = ""
  root = cwd
  with open("input","r") as fh:
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
          print(f'cd .. {cwd.name}')
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
          print(f'{line} {type(e)} {cwd.name}')
          cwd.append(e)
        continue
      line = fh.readline().strip()

  print(f'{root.size()}')

  print_size(root)

  global collected

  collected = []
  find_big_directories(root)

  collected = sorted(collected, key=lambda x: x.size())
  print(f'/ {root.size()}')
  needed = 30000000 - (70000000 - root.size())

  print(f'needed: {needed}')
  for d in collected:
  #  print(f'{d.size()} {d.path()}')
    if d.size() > needed:
      print(d)
      print(d.size())
      exit(0)

if __name__ == '__main__':
  main()
