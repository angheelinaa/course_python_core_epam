from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    try:
        value_1, value_2 = map(int, str_with_ints.split())
        result = value_1 / value_2
    except ZeroDivisionError as e:
        return f"Error code: {e}"
    except ValueError as e:
        return f"Error code: {e}"

    return result
