#!/usr/bin/python3

def main():
  MARKER_LEN=4
  marker = ""
  with open("input","r") as fh:
    buffer = fh.read()
  while True:
    for i in range(0, len(buffer)):
      ch = buffer[i]
      if ch in marker:
        marker = ""
      if len(marker) >= MARKER_LEN:
        print(i)
        exit(0)
      marker = marker + ch
if __name__ == '__main__':
  main()
