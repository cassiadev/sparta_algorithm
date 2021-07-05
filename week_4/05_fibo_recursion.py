input = 20


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)    # 매번 지난 회차의 연산도 다시 하니 효율성 떨어짐 -> 동적 계획법을 사용해 개선해보자.


print(fibo_recursion(input))  # 6765