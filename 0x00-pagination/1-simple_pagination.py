#!/usr/bin/env python3
"""
Defines class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 integer arguments and returns requested page from the dataset
        Args:
            page (int): required page number. must be a positive integer
            page_size (int): number of records per page. must be a +ve integer
        Return:
            list of lists containing required data from the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        try:
            index = index_range(page, page_size)
            """
            Returns the slice of the dataset
            corresponding to the calculated indexes.
            """
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
