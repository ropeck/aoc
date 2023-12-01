#!/usr/bin/python3
import aocd
import re
import sys

d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
for n in range(10):
    d[str(n)] = n

def first_num(text):
    m = re.search("([0-9]|one|two|three|four|five|six|seven|eight|nine)", text)
    return d[m.group(1)]

def second_num(text):
    m = re.match(".*([0-9]|one|two|three|four|five|six|seven|eight|nine)", text)
    return d[m.group(1)]

def decode(text):
    return 10* first_num(text) + second_num(text)


def main(test):
  
    mod = aocd.models.Puzzle(year=2023, day=1)
    if not test:
        data = mod.input_data
    else:
        data = mod.example_data
    t = 0
    c = 0
    for line in data.splitlines():
        c += 1
        t += decode(line)
  
    if not test:
        aocd.submit(t, part="b", day=1, year=2023)
        pass
  
if __name__ == '__main__':
  main(len(sys.argv) > 1)
