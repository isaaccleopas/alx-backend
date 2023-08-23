#!/usr/bin/env python3
"""A caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Inherit BaseCaching class"""

    def __init__(self):
        """Call the constructor of the base class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache using FIFO strategy
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.queue.pop(0)
                self.cache_data.pop(first_key)
                print("DISCARD:", first_key)

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
