#!/usr/bin/python3
import sys



def monkey_eval(m, name, h=None):
  if h == None:
    h = m['humn'][0]
  m['humn'] = [h]
  job = m[name]
  if len(job) == 1:
    return int(job[0])
  (a_name, op, b_name) = job

  a = monkey_eval(m, a_name)
  b = monkey_eval(m, b_name)
  if name == 'root':
    print(f'root: h={h} {a} cmp {b} = {b-a}')
    return int(b-a)
  return int(eval(f'{a} {op} {b}'))

def main(path):
  m = {}
  with open(path, "r") as fw:
    for line in fw:
      line = line.strip()
      (name, job) = line.split(": ")
      m[name] = job.split(" ")

  guess = 1
  prev = 0
  shout = monkey_eval(m,"root", 0)
  while shout < 0:
    prev = guess
    guess *= 2
    shout = monkey_eval(m,"root", guess)
    print(f'g {guess} s{shout}')


  mm = [guess, prev]
  mm.sort()
  (low, high) = mm
  print(f'me({low})={monkey_eval(m,"root",low)} me({high})={monkey_eval(m,"root",high)}')
  while shout:
    mid = int((high - low) / 2) + low
    guess = mid
    print(f'guess {guess}  shout {shout}  {low} {mid} {high}')
    shout = monkey_eval(m, "root", guess)
    if shout > 0:
      high = guess
    elif shout < 0:
      low = guess


  print(f'monkey eval "root"=monkey({guess}) {shout}')
  print(guess)
if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
