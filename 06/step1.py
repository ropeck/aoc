#!/usr/bin/python3

def main():
  with open("input","r") as fh:
    buffer = fh.read()
  while True:
    for i in range(4, len(buffer)):
      marker = buffer[i-4:i]
      if len(set(marker)) == 4:
        print(f'{i} {marker}')
        exit(0)
if __name__ == '__main__':
  main()
