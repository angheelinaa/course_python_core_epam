from typing import Dict
import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    def wrapper(*args, **kwargs):
        start_ts = time.time()
        result = fn(*args, **kwargs)
        end_ts = time.time()
        global execution_time
        execution_time[fn.__name__] = end_ts - start_ts
        return result

    return wrapper
