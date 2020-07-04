#pymysql安装：pip install pymysql
#在命令行启动mysql(service mysql start),在python文件中使用pymysql连接
import pymysql

db_info = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123',
    'db': 'text'
}

sqls = ['select 1', 'select VERSION']

result = []

class ConnDB:
    def __init__(self, db_info, sqls):
        self.host = db_info['host']
        self.port = db_info['port']
        self.user = db_info['user']
        self.password = db_info['password']
        self.db = db_info['db']
        self.sqls = sqls

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db,
            charset = 'utf8')

        # 获取游标
        cur = conn.cursor()
        #执行sql语句
        try:
            for command in self.sqls:
                cur.execute(command)  # 执行命令
                result.append(cur.fetchone())  # 存储结果
            cur.close()
            cur.commit()
        except:
            conn.rollback()

        # 关闭连接
        conn.close()

if __name__ == '__main__':
    conn = ConnDB(db_info, sqls)
    conn.run()
    print(result)
