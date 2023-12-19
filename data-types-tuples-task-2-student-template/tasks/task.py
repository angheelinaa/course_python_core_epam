from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    lst_pairs = [tuple([lst[i - 1], lst[i]]) for i in range(1, len(lst))]
    return lst_pairs
