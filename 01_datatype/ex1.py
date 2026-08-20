import sys
from random import randint
from collections import deque, defaultdict
input = sys.stdin.readline
print = sys.stdout.write

a = 2
b = 3
print(str(a))
print(str(b) + '\n')
print(f"{a} {b}\n")

a, b = 2, 3
print(f"{a} {b}\n")

a = b = c = 0

a, b = 2, 3
a, b = b, a

print(f"{a} {b}\n")

# name! = "pororo"
# 2name = "pororo"
# class = "test"
이름 = "뽀로로"
print(이름)

dic1 = defaultdict(int)
dic1["apple"] += 1
print(str(dic1) + '\n')

a = randint(1, 10)
print(str(a))

# crr
# rnt
# rst
# cnt
# N, M, K
# A, B, C