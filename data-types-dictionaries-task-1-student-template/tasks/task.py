from typing import Dict
from collections import Counter


def get_dict(s: str) -> Dict[str, int]:
    cnt_dct = Counter(s.lower()).most_common()
    result_dct = {k: v for k, v in cnt_dct}
    return result_dct
