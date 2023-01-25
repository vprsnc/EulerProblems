from math import gcd
from functools import reduce

our_lcm = reduce(lambda a, b: int(a * b / gcd(a,b)), range(1, 21))

print(our_lcm)
