#!/usr/bin/python3
import re
import sys

# parse beacons and sensors
# Sensor at x=3558476, y=2123614: closest beacon is at x=4305648, y=2127118

# find intersection with line at y=20000
class Beacon:
  def __init__(self, line):
    m = re.match("Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)", line.strip())
    if not m:
      print("no match: " + line)
      return
    (self.x, self.y, self.sx, self.sy) = [int(s) for s in m.groups()]

  def sensor_dist(self):
    return self.dist(self.sx, self.sy)

  def dist(self, x, y):
    return abs(self.x - x) + abs(self.y - y)

  def intersect(self, y):
    offset = self.sensor_dist() - abs(self.y - y)
    if offset < 0:
      return None
    return [self.x - offset, self.x + offset]

  def __repr__(self):
    return f'<Beacon {self.x}, {self.y} {self.sensor_dist()}>'

  def distance(self, other):
    return abs(self.x - other.x) + abs(self.y - other.y)

def intersect(b, y):
  return [i.intersect(y) for i in b]


def reduce_intersect(b, y):
  i = [n for n in intersect(b, y) if n]
  d = [i.pop()]
  print(i)
  for x in i:
    for n, c in enumerate(d.copy()):
      import pdb; pdb.set_trace()
      o = False
      if x[0] < c[0] and x[1] >= c[0]:
        d[n][0] = x[0]
        o = True
      if x[1] > c[1] and x[0] <= c[1]:
        d[n][1] = x[1]
        o = True
      if o:
        continue
      d.append(x)
  print(d)
  diff = [abs(n[0]-n[1]) for n in d]
  return sum(diff)

def main(path, y):
  b = []
  with open(path,"r") as fh:
    b = [Beacon(l) for l in fh]
  r = reduce_intersect(b, y)
  print(r)
  return r


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
    y = sys.argv[2]
  else:
    path = "input"
    y = 2000000
  main(path, y)
