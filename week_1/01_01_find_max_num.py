input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:           #파이썬은 indentation 겁나 중요함
            return num
    # return 1


result = find_max_num(input)
print(result)