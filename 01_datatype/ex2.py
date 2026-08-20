import math
import sys

# 파이썬 자료형
# 1. 기본 자료형 : 숫자형(정수형, 실수형), 불리언, 문자열
# 2.컬렉션 자료형 : 리스트, 튜플, 딕셔너리, 집합

# 숫자형(정수형)
# C언어 : char, short, int, long, long long
# int

a = 10
print(a, type(a))
print(bin(a), oct(a), hex(a))
print(ord("A"), chr(65))
x = 10 ** 1000
print(x)

a = 2 ** 31 - 1
a += 1
print(a)

# 실수형
b = 3.14
print(b, type(b))
print(math.pi)

# 실수형의 표현범위
# 부동소수점 방식 : 64비트 = 부호(1비트) + 지수부(11시트) + 가수부(52비트)  

print(sys.float_info.min)
print(sys.float_info.max)
a = 1.7e308
b = 1.8e308
print(a)
print(b)
a = float("inf")
print(a - 1)