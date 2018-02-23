from __future__ import print_function

with open("command") as infile:
    for line in infile:
        print(len(line.rstrip("\n")))
