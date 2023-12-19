from typing import Any, Dict, List, Set


def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    result = {v for i in lst for v in i.values()}
    return result
