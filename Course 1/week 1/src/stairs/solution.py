import sys

count = int(sys.argv[1])
k = count - 1
res = ''

for i in range(1, count + 1):
  res += ' '*k + i * '#' + '\n'
  k -= 1

print(res)

