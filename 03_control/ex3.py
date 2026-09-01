# for문

# for x in iterable객체:
#   ...

for i in range(5) :         # 0 ~ 4
    print(i, end = ' ')

print()
a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6) :
    print(i, end = ' ')
print()

# 1 ~ 10, 2칸씩
for i in range(1, 10, 2) :
    print(i, end = ' ')
print()

# 5, 4, 3, 2, 1 거꾸로
for i in range(5, 0, -1) :
    print(i, end = ' ')
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11) :
    tot += i
else :
    print(tot)

print(sum(range(1, 11)))

s = "hi12!@한글韓國🐸ありがとう"
for i in s :
    print(i, end = ' ')

print()
print(len(s))

# 구구단 출력
# 2 * 1 = 2
# 2 * 2 = 4

for i in range(2, 10) :
    for j in range(2, 10) :
        print(f"{i} * {j} = {i * j}")
