import os
import redis

from multiprocessing import Process

redis_conn= redis.Redis(charset='utf-8', decode_responses=True)
import time
def sub(name: str):
    pubsub = redis_conn.pubsub()
    pubsub.subscribe("my_channel")
    for message in pubsub.listen():
        if message.get("type") == "message":
            print(message)
            data = message.get("data")
            print(data)
            time.sleep(5)
        else:
            print("none")
            time.sleep(5)

if __name__ == "__main__":
    Process(target=sub, args=("reader1",)).start()