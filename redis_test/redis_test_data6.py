# Work on redis task queue..
import redis
import time
import json


# To make a connection from redis server that running before the estibiles connection..
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    # use for convert byte format response into str.
    decode_responses=True
)
print("connect with ping of redis  ---- ", redis_client.ping())

"""
# To make a connection from redis server that running before the estibiles connection with url..
redis_client = redis.from_url('redis://localhost:6379/0', decode_responses=True)
print("connect with ping of redis  ---- ", redis_client.ping())
"""
time.sleep(5)

redis_client.set('foo', 'bar')
res_data = redis_client.get('foo')
print("foo is -----> ", res_data)
print(type(res_data), '\n')

# use mset for set multiple key , valur pair data using dictionary
redis_client.mset({'data': 2, 'add': 'asksjksj'})
print("data is ----->", redis_client.get('data'), '\n')


# use the data as json formate that set into put key
redis_client.set('put', json.dumps({'data': 2, 'add': 'asksjksj'}))
data = json.loads(redis_client.get('put'))
print("found put key json data ----> ", data)
print("type of put key is ----> ",type(data), '\n')

# update the data value.
redis_client.set('data', 6)
print("update data key with  ----> ", redis_client.get('data'), '\n')


# retun None if key:data1 ,data not found
print("key data1 is  -----> ", redis_client.get('data1'), '\n')


# check key is exist or not, return 1 if exist otherwise return 0
print("key data1 not exist ---- > ", redis_client.exists('data1'))
print("key add exist -------> ", redis_client.exists('add'), '\n')


# for remove all data from redis db, use
print("flush all data -----> ", redis_client.flushdb())
print("check key add data -----> ", redis_client.get('add'), '\n')


# use the hashmap
redis_client.hset('put', 'abc', 2)
redis_client.hset('put', 'bcd', 3)
redis_client.hset('put', 'cdf', 4)
print(redis_client.hget('put', 'abc'), '\n')

# delete one key 
print("delete key is -----> ", redis_client.hdel('put', 'abc'))
print(redis_client.hgetall('put'), '\n')