print('Got this:')
print('"%s"' % input())

import sys

data = sys.stdin.readline()[:]

print(data)
print('result is: ', data, int(data) * 2)