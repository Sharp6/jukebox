import redis

class RedisClient:
    def __init__(self):
        self.name = "redis"

    def retrieve(self,key):
        return redis.get(key)
