# 불리언
# True ro False

a = True
print(a, type(a))
print(1 < 0)
print(1 > 0)
print(1 == 0)
print(1 != 0)

print("apple" > "apble")

# bool() 내장 함수
print(bool(3))
print(bool(0))
print(bool("hello"))
print(bool(""))
print(bool([1]))
print(bool([]))

# None 자료형
a = None
print(a, type(a))
print(bool(a))

if a is None :
    print("값이 없습니다.")