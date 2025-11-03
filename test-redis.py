import redis
# Connect to Redis
r = redis.Redis(host='localhost', port=6379)
# Set a key-value pair
r.set('my_key', 'Hello, Redis!')

# Get the value of the key
value = r.get('my_key')
print(value.decode('utf-8'))