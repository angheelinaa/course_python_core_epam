import time
import inspect


def write_to_file(filename, func, args, kwargs, exec_time):
    args_dict = {}
    func_args = tuple(inspect.signature(func).parameters)

    for i in range(len(args)):
        args_dict[func_args[i]] = args[i]

    args_str = ", ".join([f"{k}={v}" for k, v in args_dict.items()])
    kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])

    with open(filename, 'a') as file:
        file.write(f"{func.__name__}; args: {args_str};"
                   f" kwargs: {kwargs_str}; execution time: {exec_time} sec.\n")


def log(fn):
    def wrapper(*args, **kwargs):
        start_ts = time.time()
        result = fn(*args, **kwargs)
        end_ts = time.time()
        execution_time = round(end_ts - start_ts, 2)
        write_to_file("log.txt", fn, args, kwargs, execution_time)
        return result

    return wrapper
