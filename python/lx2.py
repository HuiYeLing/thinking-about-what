def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorials_n(N):
    for i in range(1, N + 1):
        print(f"{i}! = {factorial(i)}")

N = int(input("请输入一个正整数 N: "))
factorials_n(N)

