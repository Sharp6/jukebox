import redis

class RedisClient:
    def __init__(self):
        self.r = redis.StrictRedis(host='192.168.1.124', port=6379)

    def retrieve(self,key):
        print('Retrieving album for ' + key)
        return self.r.get(key)
