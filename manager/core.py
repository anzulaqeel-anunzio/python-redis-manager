# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import redis
import sys

# Default configuration - can be moved to env vars
HOST = 'localhost'
PORT = 6379
DB = 0

def get_connection():
    try:
        r = redis.Redis(host=HOST, port=PORT, db=DB, decode_responses=True)
        r.ping() # Check connection
        return r
    except redis.ConnectionError:
        print(f"Error: Could not connect to Redis at {HOST}:{PORT}")
        sys.exit(1)

def list_keys(pattern):
    r = get_connection()
    keys = r.keys(pattern)
    return keys

def get_key_details(key):
    r = get_connection()
    if not r.exists(key):
        return None
    
    key_type = r.type(key)
    ttl = r.ttl(key)
    
    val = None
    if key_type == 'string':
        val = r.get(key)
    elif key_type == 'list':
        val = r.lrange(key, 0, -1)
    elif key_type == 'hash':
        val = r.hgetall(key)
    elif key_type == 'set':
        val = r.smembers(key)
    else:
        val = f"<{key_type}> (Value extraction not implemented for CLI)"

    return {
        "type": key_type,
        "ttl": ttl,
        "value": val
    }

def delete_key(key):
    r = get_connection()
    return r.delete(key)

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
