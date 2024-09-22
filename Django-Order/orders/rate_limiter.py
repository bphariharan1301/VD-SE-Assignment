import time
from django.core.cache import cache


class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window

    def allow_request(self, user_id):
        current_time = time.time()
        cache_key = f"rate_limit_{user_id}"

        # Get timestamps from the cache
        timestamps = cache.get(cache_key, [])

        # Remove old timestamps
        timestamps = [ts for ts in timestamps if current_time - ts < self.time_window]

        # Check if user is allowed to make a request
        if len(timestamps) < self.max_requests:
            timestamps.append(current_time)
            cache.set(cache_key, timestamps, timeout=self.time_window)
            return True
        else:
            return False
