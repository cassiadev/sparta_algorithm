finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2 # 몫 표현
    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
# k회 탐색하면 N / 2**k 개의 자료가 남음. 1개 남았을 때 1 = n / 2**k 이니까 k = log 2의 N !!
# 따라서 이분탐색의 시간복잡도는 O(log 2의 N)
