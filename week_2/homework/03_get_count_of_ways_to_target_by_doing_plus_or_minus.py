numbers = [1,1,1,1,1]
target_number = 3

result_count = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    # 길이가 N인 배열에서 더하거나 뺀 모든 경우의 수는 길이 N-1인 배열에서 마지막 원소를 더하거나 뺀 경우의 수 + 이번에 새로 추가하는 방식으로
    if current_index == len(array):  # 탈출조건!
        if current_sum == target:
            global result_count
            result_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - array[current_index])
    return


result_array = []


def get_all_ways_to_by_doing_plus_or_minus(array, target, current_index, current_sum, all_ways):
    if current_index == len(numbers):
        all_ways.append(current_sum)
        return
    get_all_ways_to_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum + numbers[current_index], all_ways
    )
    get_all_ways_to_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum - numbers[current_index], all_ways
    )


print(get_all_ways_to_by_doing_plus_or_minus(numbers, target_number, 0, 0, result_array))
print(result_array)
print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, result_count))  # 5를 반환해야 합니다!
print(result_count)