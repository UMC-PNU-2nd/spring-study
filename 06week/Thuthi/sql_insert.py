import pymysql
import datetime

import random

host = "umcdb.ckjyatpmv9xd.us-west-2.rds.amazonaws.com"
user = "thuthi"
pw = "whxnxl55;;"
db = "Umc"
charset = "utf8"

def main():
    connection = pymysql.connect(host=host, user=user, password=pw, db=db, charset=charset)
    cursor = connection.cursor()
    sql = """
        Insert Ignore into Follow(followerIdx, followIdx, createdAt, updatedAt) values (%s, %s, %s, %s)
    """
    values = []
    for _ in range(0, 100000000): 
        a = random.randrange(1, 10000001)
        b = random.randrange(1, 10000001)


        values.append((a, b, datetime.datetime.now(), datetime.datetime.now()))
        if (values.__len__() % 10000 == 0):
            print(values.__len__())
            cursor.executemany(sql, values)
            connection.commit()
            values.clear()
    
    connection.close()

main()
