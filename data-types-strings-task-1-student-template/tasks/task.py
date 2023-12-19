def get_fractions(a_b: str, c_b: str) -> str:
    a_b_list = a_b.split("/")
    c_b_list = c_b.split("/")

    res_sum = int(a_b_list[0]) + int(c_b_list[0])

    return f'{a_b} + {c_b} = {res_sum}/{a_b_list[1]}'
