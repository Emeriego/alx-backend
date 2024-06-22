#!/usr/bin/env python3
"""
defines index_range helper function for pagination purpose
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes 2 integer arguments and returns a tuple of 2 integers,
    the start index and the end index.
    Args:
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)



   

