from typing import List


def multiply(row:int, column_start:int, column_end:int):
    lst = [row * c for c in range(column_start, column_end + 1)]
    return lst


def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    result = [
        multiply(r, column_start, column_end)
        for r in range(row_start, row_end + 1)
    ]
    return result
