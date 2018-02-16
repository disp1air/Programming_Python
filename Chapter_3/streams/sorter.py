import sys

lines = sys.stdin.readlines()
print(lines)
lines.sort()

for line in lines:
    print(line, end='')