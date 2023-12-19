from typing import Any, List


def linear_seq(sequence: List[Any]) -> List[Any]:
    result = []
    for i in sequence:
        if isinstance(i, int):
            result.append(i)
        else:
            result.extend(linear_seq(i))
    return result
