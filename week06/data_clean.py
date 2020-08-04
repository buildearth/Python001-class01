

def data_clean():
    import pandas as pd
    import pymysql
    star_to_number = {
        '力荐': 5,
        '很差': 4,
        '推荐': 3,
        '较差': 2,
        '还行': 1,
    }

    conn = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '123',
        db = 'movies'
        )

    sql = "select * from Douban"

    df = pd.read_sql(sql, conn)
    df['new_star'] = df['star'].map(star_to_number)

    # df.to_sql('Douban_new', conn)
    df.to_sql(name="Douban_new",
    con='mysql+pymysql://root:123@localhost:3306/movies?charset=utf8',
    if_exists='append', index=False)
    conn.close()


if __name__ == '__main__':
    data_clean()
# create table Douban_new(
#         id serial not null primary key,
#         star varchar(30),
#         short varchar(300),
#         new_star int
#     )ENGINE=InnoDB DEFAULT CHARSET=utf8;
