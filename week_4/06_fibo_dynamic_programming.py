import sys

input = 2000

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)  # Top-down 방식. 반대는 Bottom-up 방식
    fibo_memo[n] = nth_fibo

    return nth_fibo # 200은 되는데...2000은 안되네 그래도


sys.setrecursionlimit(2000)
print(fibo_dynamic_programming(input, memo))