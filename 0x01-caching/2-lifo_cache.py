#!/usr/bin/env python3
"""A caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Inherit BaseCaching class"""

    def __init__(self):
        """Call the constructor of the base class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache using LIFO strategy
        """
        if key is not None and item is not None:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key = self.queue.pop()
                self.cache_data.pop(last_key)
                print("DISCARD:", last_key)

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
