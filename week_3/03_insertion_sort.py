input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i -j -1] > array[i -j]:
                array[i - j - 1], array[i -j] = array[i -j], array[i -j -1]
            else:
                break   # 얘 덕분에 시간복잡도가 임의 상수로 줄어들 수 있음
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!