#!/usr/bin/python3
import aocd
import re
import sys

def convert_num(text):
    d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    def inner(m):
        return str(d[m.group(1)])
    text = re.sub('(one|two|three|four|five|six|seven|eight|nine)', inner, text, count=1)
    dig = 'one|two|three|four|five|six|seven|eight|nine'[::-1]
    r = text[::-1]
    def inner_rev(m):
        print(m.group(0), m.group(1), m.group(1)[::-1])
        return str(d[m.group(1)[::-1]])
    text2 = re.sub(f'({dig})', inner_rev, text[::-1], count=1)
    text2 = text2[::-1]
    return text2

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
    total = 0
  # with open(path, "r") as fh:
  #   line = fh.readline().strip()
  #   while True:
  
  
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
