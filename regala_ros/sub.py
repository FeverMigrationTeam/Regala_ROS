import redis

from multiprocessing import Process
import json

redis_conn= redis.Redis(charset='utf-8', decode_responses=True)

import time
# rtsp_test.func()
def rtsp_func():
    time.sleep(3)
    print('turn on complete!')

# video_recorder.func()
def recorder_func(user_id, equipment_id):
    time.sleep(10)
    print(f'record start\nuser_id: {user_id},\nequipment: {equipment_id}')

# google_upload.func()
def upload_func():
    time.sleep(5)
    print(f'upload success, close session.')

def sub():
    pubsub = redis_conn.pubsub()
    pubsub.subscribe("regalaData")
    for message in pubsub.listen():
        if message.get("type") == "message":
            data = json.loads(message.get("data"))
            user_id = data.get("user_id")
            equipment_id = data.get("equipment_id")
            rtsp_func()
            recorder_func(user_id, equipment_id)
            upload_func()
        else:
            print("Message listening...")

if __name__ == "__main__":
    p = Process(target=sub)
    p.start()
