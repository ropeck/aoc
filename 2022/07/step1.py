#!/usr/bin/python3
import re

class Entry:
  def __init__(self, name, size, parent):
    self.name = name
    self.byte_size = int(size)
    self.parent = parent
    self.entries = {}

  def size(self):
    return self.byte_size

  def print_size(self, indent=0):
    print(f'{indent*"  "}- {self}')

  def path(self):
    if self.parent:
      return f'{self.parent.path()}/{self.name}'
    else:
      return ""
  def find_big_directories(self):
    return
  def __str__(self):
    return f'{self.name} (file, size={self.size()})'
  def isDir(self):
    return False

class Dir(Entry):
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.entries = {}

  def isDir(self):
    return True

  def size(self):
    return sum([x.size() for x in self.entries.values()])

  def append(self, entry):
    self.entries[entry.name]=entry

  def __str__(self):
    return f'{self.name} (dir)'

  def print_size(self, indent=0):

    super().print_size(indent)
    for f in self.entries.values():
      f.print_size(indent+1)

  def find_big_directories(self):
    global total_size
    if self.size() < 100000:
      print(f'{self.path()} {self.size()}')
      total_size += self.size()
    for f in self.entries.values():
      f.find_big_directories()

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

  root.print_size()

  global total_size

  total_size = 0
  root.find_big_directories()
  print(f'total size {total_size}')

if __name__ == '__main__':
  main()
