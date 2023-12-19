from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    result = []

    for str_elem in str_list:
        if str_elem not in result:
            result.append(str_elem)
    result.sort()
    return result
