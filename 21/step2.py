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

  guess = 10
  prev = monkey_eval(m,"root", 0)
  while True:
    shout = monkey_eval(m,"root", guess)
    if shout == 0:
      break
    if prev * shout > 0:
      guess = guess * 2
      prev = shout
    else:
      break
  low = prev
  high = guess
  while shout:
    if shout > 0:
      print("low")
      low = int((low + high) / 2)
    else:
      print("high")
      high = int((low + high) / 2)
    shout = monkey_eval(m, "root", int((low + high)/2))


  print(f'monkey eval "root"=monkey({guess}) {shout}')
  print(guess)
if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
