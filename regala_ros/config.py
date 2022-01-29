db = {
    'user': 'fever',
    'password': 'fever1234',
    'host': 'feverdb.cy76xlw8fwhe.ap-northeast-2.rds.amazonaws.com',
    'port': '3306',
    'database': 'playcanival'
}

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8".format(
    db['user'],
    db['password'],
    db['host'],
    db['port'],
    db['database']
)
