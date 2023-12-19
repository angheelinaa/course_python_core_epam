from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    len_str = len(s)
    split_lst = []
    start = 0
    for index in indexes:
        if index >= len_str:
            split_lst.append(s[start:])
            return split_lst

        split_lst.append(s[start:index])
        start = index
    split_lst.append(s[index:])
    return split_lst
