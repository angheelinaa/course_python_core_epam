from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    result = {i: i**2 for i in range(1, num+1)}
    return result
