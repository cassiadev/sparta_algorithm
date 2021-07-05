input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alpahbet_array = ["a", "b", "c", "d", "e", "f", "g"]
    max_occurence = 0
    max_alphabet = alpahbet_array[0]

    for alphabet in alpahbet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurence:
            max_occurence = occurrence
            max_alphabet = alphabet

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)