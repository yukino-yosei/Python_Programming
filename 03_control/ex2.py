# 반복문 : while문, for문

# while문
# 1 ~ 10까지의 반복 출력

i = 1
while i <= 10 :
    print(i, end = ' ')
    i += 1
    if i > 5 :
        break
else :
    print("End")
print()

num = [1, 3, 5, 7, 9]
target = 2
i = 0

while i < len(num) :
    if num[i] == target :
        print(f"{i}번째")
        break
    i += 1
else :
    print("없음")

# 1 ~ 10까지의 합
i = 1
tot = 0
while i <= 10 :
    i += 1
    if i % 2 == 1 :
        continue
    tot += i
else :
    print(tot)