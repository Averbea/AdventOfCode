import inspect
import os
import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'{func.__name__} Took {total_time:.10f} seconds')
        return result

    return timeit_wrapper


def read_input_file(test=False):
    """parses the input file and returns the result"""
    filename = "/testinput.txt" if test else "/input.txt"
    calling_file_folder = os.path.dirname(inspect.stack()[1].filename)
    with open(calling_file_folder + filename, 'r', encoding="UTF-8") as input_file:
        return input_file.read()
