
def decorator_apply(lambda_func):
    def decorator(fn):
        def wrapper(arg):
            return fn(lambda_func(arg))

        return wrapper

    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    return num
cd