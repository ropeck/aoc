#!/usr/bin/python3
import sys



def monkey_eval(m, name):
  job = m[name]
  if len(job) == 1:
    return int(job[0])
  (a_name, op, b_name) = job
  a = monkey_eval(m, a_name)
  b = monkey_eval(m, b_name)
  return eval(f'{a} {op} {b}')

def main(path):
  m = {}
  with open(path, "r") as fw:
    for line in fw:
      line = line.strip()
      (name, job) = line.split(": ")
      m[name] = job.split(" ")
  val = monkey_eval(m, "root")
  print(f'monkey eval "root"={val}')
  return val


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
