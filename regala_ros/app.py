# from src import rtsp_test, video_stitcher, video_recorder, google_drive_test
from flask import Flask, request, jsonify
import config as config
import redis
import json
import pymysql

app = Flask (__name__)
red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)

db_config = config.db
db = pymysql.connect(
    user=db_config['user'],
    passwd=db_config['password'],
    host=db_config['host'],
    db=db_config['database'],
    charset='utf8'
)
cur = db.cursor()

@app.route('/recordRegala', methods = ['POST'])
def record_regala():
    req_body = request.json
    user_id = req_body.get("user_id")
    equipment_id = req_body.get("equipment_id")

    # userId로 유저 validation, get_by_equipment_id
    get_user_sql = "SELECT * FROM user WHERE user_idx=%s;"
    cur.execute(get_user_sql, user_id)

    get_user = cur.fetchall()

    if not get_user:
        return jsonify({"status": 403, "message": "접근 권한 없음"})
    
    get_equipment_sql = "SELECT * FROM equipment WHERE equipment_idx=%s;"
    cur.execute(get_equipment_sql, equipment_id)

    get_equipment = cur.fetchall()

    if not get_equipment:
        return jsonify({"status": 404, "message": "등록되지 않은 장치입니다"})
    
    red.publish('regalaData', json.dumps(req_body))

    update_equipment_status_sql = '''
        UPDATE equipment
        SET equipment_service_state = 1
        WHERE equipment_idx=%s;
    '''
    cur.execute(update_equipment_status_sql, equipment_id)
    db.commit()

    return jsonify({"status": 200, "request":req_body})

if __name__=="__main__":
    app.run('localhost', 8080)
