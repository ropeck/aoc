#!/usr/bin/python3

def main():
  MARKER_LEN=4
  with open("input","r") as fh:
    buffer = fh.read()
  while True:
    for i in range(MARKER_LEN, len(buffer)):
      marker = buffer[i-MARKER_LEN:i]
      if len(set(marker)) == MARKER_LEN:
        print(f'{i} {marker}')
        exit(0)
if __name__ == '__main__':
  main()
