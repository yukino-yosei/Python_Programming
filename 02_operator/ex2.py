# 비트 연산자
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(40 >> b)
print(~a)

# 맴버십 연산자
print("a" in "apple")
print(3 in [1, 2, 3])

# 삼항 연산자
# int max = a > b ? a : b;
max = a if a > b else b

# a가 짝수면 "짝수", 홀수면 "홀수"
print("짝수" if a % 2 == 0 else "홀수")

# 90점 이상이면 A
# 80점 이상이면 B
# 70점 이상이면 C
# 70점 미만이면 D
score = 85

grade = None
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(grade)