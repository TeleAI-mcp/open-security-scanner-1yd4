"""Cache module for the security scanner."""

class Cache:
    def __init__(self):
        self._store = {}
    
    def get(self, key):
        return self._store.get(key)
    
    def set(self, key, value):
        self._store[key] = value
    
    def clear(self):
        self._store.clear()
