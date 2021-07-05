input = 20


def find_prime_list_under_number(number):
    # My try
    prime_list = []
    # for i in range(2, number + 1):
    #     for j in range(2, i):
    #         if i % j == 0:
    #             break
    #     else:
    #         prime_list.append(i)

    # Improvement 1
    # for i in range(2, number + 1):
    #     for j in prime_list:    # 소수들만의 리스트 안에서 찾으면 됨
    #         if i % j == 0:
    #             break
    #     else:
    #         prime_list.append(i)

    # Improvement 2
    for i in range(2, number + 1):
        for j in prime_list:    # 임의의 자연수는 자신의 제곱근보다 크지 않은 어떠한 소수로도 나누어 떨어지지 않는다
            if i % j == 0 and j * j <= i:
                break
        else:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)