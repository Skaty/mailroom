"""
Useful decorators
"""

import functools, logging, traceback

def suppress_exceptions(return_value):
    """
    Suppresses all exceptions and returns the specified return
    value instead of throwing it
    """
    def inner_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                logging.warn('Exception caught in suppress_exceptions decorator')
                logging.warn(traceback.format_exc())
                return return_value
        return wrapper
    return inner_decorator
