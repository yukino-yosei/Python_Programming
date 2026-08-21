# 문자열
# "", '

a = 'python'
a = "python"
print(a, type(a))

# I'll be back
print("I'll be back")
print('I\'ll be back')

multiline = """
Life is short
You need Python
"""

print(multiline)

def func() :
    """이 함수는 테스트용입니다."""
    pass

print(func.__doc__)

#문자열 연결
print("Hello" + " Python")
print("Hello" * 10)
print("*" * 50)
# print("Hello" + 10)
print("Hello" + str(10))

print("10" + "2")
print(int("10") + int("2"))