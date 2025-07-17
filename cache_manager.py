"""
Cache manager for expensive system operations.
"""

import time
from functools import wraps

class CacheManager:
    _cache = {}
    
    @classmethod
    def cached(cls, ttl=10):
        """
        Decorator for caching function results.
        
        Args:
            ttl: Time to live for cache entries in seconds
            
        Returns:
            Decorated function with caching behavior
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Create a cache key from function name and arguments
                key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
                
                # Check if we have a cached result and it's still valid
                now = time.time()
                if key in cls._cache and now - cls._cache[key]['timestamp'] < ttl:
                    return cls._cache[key]['result']
                
                # Call the function and cache the result
                result = func(*args, **kwargs)
                cls._cache[key] = {
                    'result': result,
                    'timestamp': now
                }
                
                return result
            return wrapper
        return decorator
