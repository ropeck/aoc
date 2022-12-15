#!/usr/bin/python3
import sys

# parse beacons and sensors
# Sensor at x=3558476, y=2123614: closest beacon is at x=4305648, y=2127118

# find intersection with line at y=20000
class Beacon:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def distance(self, other):
    return abs(self.x - other.x) + abs(self.y - other.y)
  def intersecting_slice(self, y):
    # somehow find the start and end of the part that is within range

def main(path):
  total = 0
  # with open("input","r") as fh:
  #   line = fh.readline().strip()
  #   while True:

  for line in open(path,"r"):
    pass
  print(f'total: {total}')

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
