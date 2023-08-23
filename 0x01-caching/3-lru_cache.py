#!/usr/bin/env python3
"""A caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Inherit BaseCaching class"""

    def __init__(self):
        """Call the constructor of the base class"""
        super().__init__()
        self.lru_order = []

    def update_lru_order(self, key):
        """Update LRU order"""
        if key in self.lru_order:
            self.lru_order.remove(key)
        self.lru_order.insert(0, key)

    def remove_lru_item(self):
        """Remove LRU order"""
        if self.lru_order:
            lru_key = self.lru_order.pop()
            self.cache_data.pop(lru_key, None)

    def put(self, key, item):
        """ Add an item in the cache using LRU strategy
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.remove_lru_item()
                print("DISCARD:", key)

            self.cache_data[key] = item
            self.update_lru_order(key)

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None and key in self.cache_data:
            self.update_lru_order(key)
            return self.cache_data[key]
        else:
            return None
