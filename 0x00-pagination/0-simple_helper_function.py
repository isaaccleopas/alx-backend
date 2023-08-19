#!/usr/bin/env python3
"""Takes two integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Takes 2 arguements and returns start and end indices as tuple
    """
    start = (page -1) * page_size
    end = start + page_size
    return (start, end)
