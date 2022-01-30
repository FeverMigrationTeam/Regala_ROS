# pymysql 설정
db = {
    'user': 'fever',
    'password': 'fever1234',
    'host': 'feverdb.cy76xlw8fwhe.ap-northeast-2.rds.amazonaws.com',
    'port': '3306',
    'database': 'playcanival'
}

# REDIS pubsub 설정
REDIS = {
    'ip': '127.0.0.1',  # pubsub은 로컬에서 처리 가능하기 때문에 127.0.0.1로도 접속 가능할 것 같습니다
    'port': 6379,
    'charset': 'utf-8',
    'decode_responses': True
}

# 안쓰는 db설정 (flask sqlarchemy 사용시 이용하는 설정)
DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8".format(
    db['user'],
    db['password'],
    db['host'],
    db['port'],
    db['database']
)
