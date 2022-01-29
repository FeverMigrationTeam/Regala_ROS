from distutils.command.upload import upload
# from src import rtsp_test, video_stitcher, video_recorder, google_drive_test
from flask import Flask, request, jsonify
import config
from sqlalchemy import create_engine, text
import redis
import json

app = Flask (__name__)
red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
app.config.from_pyfile('config.py')

database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
app.database = database

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

@app.route('/recordRegala', methods = ['POST'])
def record_regala():
    req_body = request.json
    
    red.publish('regalaData', json.dumps(req_body))

    return req_body

if __name__ == '__main__':
    app.run('localhost', 8080)
