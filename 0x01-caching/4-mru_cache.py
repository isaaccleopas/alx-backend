#!/usr/bin/env python3
"""A caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Inherit BaseCaching class"""

    def __init__(self):
        """Call the constructor of the base class"""
        super().__init__()
        self.mru_order = []

    def update_mru_order(self, key):
        """Update MRU"""
        if key in self.mru_order:
            self.mru_order.remove(key)
        self.mru_order.append(key)

    def remove_mru_item(self):
        """Remove MRU"""
        if self.mru_order:
            mru_key = self.mru_order.pop()
            self.cache_data.pop(mru_key, None)

    def put(self, key, item):
        """ Add an item in the cache using MRU strategy
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.mru_order.pop()
                self.cache_data.pop(mru_key)
                print("DISCARD:", mru_key)

            self.cache_data[key] = item
            self.update_mru_order(key)

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            # Update MRU order
            self.update_mru_order(key)
            return self.cache_data[key]
        else:
            return None
