from typing import List
from functools import reduce


def foo(nums: List[int]) -> List[int]:
    product_result = reduce(lambda x, y: x * y, nums)
    result = [int(product_result / i) for i in nums]
    return result
