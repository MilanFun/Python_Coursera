import sys
import math

# a*x^2 + b*x + c = 0

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b**2 - 4*a*c
d_sqrt = math.sqrt(d)

print(int((-b + d_sqrt)/(2*a)))
print(int((-b - d_sqrt)/(2*a)))


