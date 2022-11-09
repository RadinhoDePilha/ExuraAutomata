from typing import Callable, Optional

def typeerror_pass(func):
    """
    A most beautiful exception treatment
    Args:
        func (Callable):
    """
    def abs_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
            
        except TypeError as error:
                pass
    return abs_func


def valueerror_pass(func):
    """
    A most beautiful exception treatment
    Args:
        func (Callable):
    """
    def abs_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
            
        except ValueError as error:
                pass
    return abs_func


def runtime_pass(func):
    """
    A most beautiful exception treatment
    Args:
        func (Callable):
    """
    def abs_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
            
        except RuntimeError as error:
                pass
    return abs_func