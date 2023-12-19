def get_longest_word(s: str) -> str:
    result_list = s.split()

    longest_word = max(result_list, key=len)

    return longest_word
