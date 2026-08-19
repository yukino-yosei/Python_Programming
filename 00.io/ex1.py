import sys
from collections import deque, defaultdict
import itertools
input = sys.stdin.readline
print = sys.stdout.write

a = input()
print(a)
print(type(a))

a = input()
int(a)
print(type(a))

a = int(input())
print(a, type(a))

b = float(input())
print(b, type(b))

a = int(input())
b = int(input())
print(a, b)

a = input().split()
print(a)
a = list(map(int, a))
print(a)

a, b = map(int, input().split())
print(a, b)

a, b, c = map(int, input().split())
print(a, b, c)

a = list(map(int, input().split()))
print("".join(str(a)))