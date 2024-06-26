#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.order = []

    # def put(self, key, item):
    #     """ Check if cache is full.
    #     # Find the first item added to the cache (FIFO)
    #     # Remove the oldest item
    #     # Add new item to cache
    #     """
    #     if len(self.cache_data) >= self.MAX_ITEMS:
    #         first_key = next(iter(self.cache_data))
    #         print(f"DISCARD: {first_key}\n")
    #         del self.cache_data[first_key]
        
    #     self.cache_data[key] = item

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is None and key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
