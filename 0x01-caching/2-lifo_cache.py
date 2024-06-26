#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    it inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method and an order list
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a key-value pair
        it checks if the cache is full and removes the last item
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1] 
            if key in self.order: 
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Return value linked to key.
            If key is None or doesn't exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
