import functools


def validate(fn):
    """
    Validate arguments in origin function: from 0(int) to 256(int) inclusive
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg < 0 or arg > 256:
                return "Function call is not valid!"
        for kwarg in kwargs.values():
            if not isinstance(kwarg, int) or kwarg < 0 or kwarg > 256:
                return "Function call is not valid!"
        return fn(*args, **kwargs)

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return "Pixel created!"
