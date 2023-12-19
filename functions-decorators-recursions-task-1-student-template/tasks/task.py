from typing import List, Tuple, Union
import functools


def repack_seq(seq, res):
    for i in seq:
        if isinstance(i, int):
            res.append(i)
        else:
            repack_seq(i, res)


def seq_sum(sequence: Union[List, Tuple]) -> int:
    result = []
    repack_seq(sequence, result)
    return functools.reduce(lambda x, y: x + y, result, 0)
