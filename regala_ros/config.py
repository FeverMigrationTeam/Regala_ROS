db = {
    'user': 'admin',
    'password': 'admin1234',
    'host': 'fever-db.cy76xlw8fwhe.ap-northeast-2.rds.amazonaws.com',
    'port': '3306',
    'database': 'fever'
}

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8".format(
    db['user'],
    db['password'],
    db['host'],
    db['port'],
    db['database']
)
