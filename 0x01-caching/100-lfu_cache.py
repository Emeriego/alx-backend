#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a LFU caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                """get the smallest value in the frequency
                and add them to the list lfu_keys if they are more than one
                """
                lfu = min(self.frequency.values())
                lfu_keys = []
                for k, v in self.frequency.items():
                    if v == lfu:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    # if the least frequently used is more than one we apply
                    # least recently used to break the tie
                    lru_lfu = {}
                    for k in lfu_keys:
                        lru_lfu[k] = self.usage.index(k)
                    least_recently_used = min(lru_lfu.values())
                    least_recently_freguently_used = self.usage[least_recently_used]
                else:
                    least_recently_freguently_used = lfu_keys[0]

                print("DISCARD: {}".format(least_recently_freguently_used))
                del self.cache_data[least_recently_freguently_used]
                del self.usage[self.usage.index(least_recently_freguently_used)]
                del self.frequency[least_recently_freguently_used]
            # update usage frequency
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
