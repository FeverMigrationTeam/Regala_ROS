import requests
import json
import redis
from multiprocessing import Process

red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
URL = 'http://localhost:8080/recordRegala'

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

def stream():
    print('start stream')
    # red.publish('regalaData', "{'user_id': 1, 'equipment_id': 2}")
    sub = red.pubsub()
    sub.subscribe('regalaData')
    message = sub.get_message()
    if message:
        data = message.get("data")
        print(message)
        time.sleep(5)
    else:
        print('sleep now...')
        time.sleep(5)

if __name__=="__main__":
    while True:
        stream()
