from typing import List, Dict


def combine_dicts(*args: List[Dict[str, int]]) -> Dict[str, int]:
    result = {}
    for arg in args:
        for key, value in arg.items():
            if result.get(key) is None:
                result[key] = value
            else:
                result[key] += value
    return result
