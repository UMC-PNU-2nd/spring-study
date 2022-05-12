import pymysql
import datetime
import string
import random

USER_TABLE_SIZE = 5000000
FOLLOW_TABLE_SIZE = 20000000
POST_TABLE_SIZE = 20000000
POST_LIKE_TABLE_SIZE = 100000000
POST_IMG_URL_TABLE_SIZE = 100000000
COMMENT_TABLE_SIZE = 100000000
COMMENT_LIKE_TABLE_SIZE = 500000000

host = "localhost"
port = 3306
user = "thuthi"
pw = "whxnxl55;;"
db = "testdb"
charset = "utf8"

def randomString(len):
    string_pool = string.ascii_letters + string.digits
    result = ""
    for _ in range(len):
        result += random.choice(string_pool)
    return result

def insert_user():
    connection = pymysql.connect(host=host, user=user, password=pw, db=db, charset=charset, port=port)
    cursor = connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("SET UNIQUE_CHECKS = 0;")
    connection.commit()
    sql = """
        Insert into User(nickname, name, profileUrl, websiteUrl, introduce, status, createdAt, updatedAt, email) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = []
    for _ in range(0, USER_TABLE_SIZE): 
        nickname = randomString(10)
        name = randomString(10)
        profileUrl = randomString(30)
        websiteUrl = randomString(30)
        introduce = randomString(30)
        status = 'ACTIVE'
        createdAt = datetime.datetime.now()
        updatedAt = datetime.datetime.now()
        email = randomString(10) + '@' + randomString(10) + '.com'

        values.append((
            nickname, 
            name,
            profileUrl,
            websiteUrl,
            introduce,
            status,
            createdAt,
            updatedAt,
            email
        ))

        if (values.__len__() % 100000 == 0):
            print(values.__len__(), flush=True)
            cursor.executemany(sql, values)
            connection.commit()
            values.clear()

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cursor.execute("SET UNIQUE_CHECKS = 1;")
    connection.commit()
    
    connection.close()

def insert_follow():
    connection = pymysql.connect(host=host, user=user, password=pw, db=db, charset=charset, port=port)
    cursor = connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("SET UNIQUE_CHECKS = 0;")
    connection.commit()
    sql = """
        Insert into Follow(followerIdx, followIdx, status, createdAt, updatedAt) values (%s, %s, %s, %s, %s)
    """
    values = []
    inserted = set()
    for _ in range(0, FOLLOW_TABLE_SIZE): 
        followerIdx = random.randint(1, USER_TABLE_SIZE)
        followIdx = random.randint(1, USER_TABLE_SIZE)
        if (followerIdx, followIdx) in inserted :
            continue
        inserted.add((followerIdx, followIdx))

        status = 'ACTIVE'
        createdAt = datetime.datetime.now()
        updatedAt = datetime.datetime.now()

        values.append((
            followerIdx, 
            followIdx,
            status,
            createdAt,
            updatedAt,
        ))

        if (values.__len__() % (POST_TABLE_SIZE / 10) == 0):
            print(values.__len__(), flush=True)
            cursor.executemany(sql, values)
            connection.commit()
            values.clear()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cursor.execute("SET UNIQUE_CHECKS = 1;")
    connection.commit()
    connection.close()

def insert_post():
    connection = pymysql.connect(host=host, user=user, password=pw, db=db, charset=charset, port=port)
    cursor = connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("SET UNIQUE_CHECKS = 0;")
    connection.commit()
    sql = """
        Insert into Post(userIdx, content, status, createdAt, updatedAt) values (%s, %s, %s, %s, %s)
    """
    values = []
    for _ in range(0, POST_TABLE_SIZE): 
        userIdx = random.randint(1, USER_TABLE_SIZE)
        content = randomString(30)
        status = 'ACTIVE'
        createdAt = datetime.datetime.now()
        updatedAt = datetime.datetime.now()

        values.append((
            userIdx, 
            content,
            status,
            createdAt,
            updatedAt,
        ))

        if (values.__len__() % (POST_TABLE_SIZE / 10) == 0):
            print(values.__len__(), flush=True)
            cursor.executemany(sql, values)
            connection.commit()
            values.clear()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cursor.execute("SET UNIQUE_CHECKS = 1;")
    connection.commit()
    connection.close()

def insert_postLike():
    connection = pymysql.connect(host=host, user=user, password=pw, db=db, charset=charset, port=port)
    cursor = connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("SET UNIQUE_CHECKS = 0;")
    connection.commit()
    sql = """
        Insert into PostLike(postIdx, userIdx, status, createdAt, updatedAt) values (%s, %s, %s, %s, %s)
    """
    values = []
    inserted = set()
    for _ in range(0, POST_LIKE_TABLE_SIZE): 
        postIdx = random.randint(1, POST_TABLE_SIZE)
        userIdx = random.randint(1, USER_TABLE_SIZE)
        if (postIdx, userIdx) in inserted :
            continue
        inserted.add((postIdx, userIdx))

        status = 'ACTIVE'
        createdAt = datetime.datetime.now()
        updatedAt = datetime.datetime.now()

        values.append((
            postIdx, 
            userIdx,
            status,
            createdAt,
            updatedAt,
        ))

        if (values.__len__() % (POST_LIKE_TABLE_SIZE / 100) == 0):
            print(values.__len__(), flush=True)
            cursor.executemany(sql, values)
            connection.commit()
            values.clear()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cursor.execute("SET UNIQUE_CHECKS = 1;")
    connection.commit()
    connection.close()

def insert_postImgUrl():
    connection = pymysql.connect(host=host, user=user, password=pw, db=db, charset=charset, port=port)
    cursor = connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("SET UNIQUE_CHECKS = 0;")
    connection.commit()
    sql = """
        Insert into PostImgUrl(postIdx, imgUrl, status, createdAt, updatedAt) values (%s, %s, %s, %s, %s)
    """
    values = []
    for _ in range(0, POST_IMG_URL_TABLE_SIZE): 
        postIdx = random.randint(1, POST_TABLE_SIZE)
        imgUrl = randomString(30)
        status = 'ACTIVE'
        createdAt = datetime.datetime.now()
        updatedAt = datetime.datetime.now()

        values.append((
            postIdx, 
            imgUrl,
            status,
            createdAt,
            updatedAt,
        ))

        if (values.__len__() % (POST_IMG_URL_TABLE_SIZE / 100) == 0):
            print(values.__len__(), flush=True)
            cursor.executemany(sql, values)
            connection.commit()
            values.clear()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cursor.execute("SET UNIQUE_CHECKS = 1;")
    connection.commit()
    connection.close()

def insert_comment():
    connection = pymysql.connect(host=host, user=user, password=pw, db=db, charset=charset, port=port)
    cursor = connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("SET UNIQUE_CHECKS = 0;")
    connection.commit()
    sql = """
        Insert into Comment(userIdx, postIdx, content, parentComment, status, createdAt, updatedAt) values (%s, %s, %s, %s, %s, %s, %s)
    """
    values = []
    for _ in range(0, COMMENT_TABLE_SIZE): 
        userIdx = random.randint(1, USER_TABLE_SIZE)
        postIdx = random.randint(1, POST_TABLE_SIZE)
        content = randomString(30)
        parentComment = 0
        status = 'ACTIVE'
        createdAt = datetime.datetime.now()
        updatedAt = datetime.datetime.now()

        values.append((
            userIdx, 
            postIdx,
            content,
            parentComment,
            status,
            createdAt,
            updatedAt,
        ))

        if (values.__len__() % (COMMENT_TABLE_SIZE / 100) == 0):
            print(values.__len__(), flush=True)
            cursor.executemany(sql, values)
            connection.commit()
            values.clear()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cursor.execute("SET UNIQUE_CHECKS = 1;")
    connection.commit()
    connection.close()

def insert_commentLike():
    connection = pymysql.connect(host=host, user=user, password=pw, db=db, charset=charset, port=port)
    cursor = connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("SET UNIQUE_CHECKS = 0;")
    connection.commit()
    sql = """
        Insert into CommentLike(userIdx, commentIdx, status, createdAt, updatedAt) values (%s, %s, %s, %s, %s)
    """
    values = []
    inserted = set()
    for _ in range(0, COMMENT_LIKE_TABLE_SIZE): 
        userIdx = random.randint(1, USER_TABLE_SIZE)
        commentIdx = random.randint(1, COMMENT_TABLE_SIZE)
        if (userIdx, commentIdx) in inserted :
            continue
        inserted.add((userIdx, commentIdx))

        status = 'ACTIVE'
        createdAt = datetime.datetime.now()
        updatedAt = datetime.datetime.now()

        values.append((
            userIdx, 
            commentIdx,
            status,
            createdAt,
            updatedAt,
        ))

        if (values.__len__() % (COMMENT_LIKE_TABLE_SIZE / 500) == 0):
            print(values.__len__(), flush=True)
            cursor.executemany(sql, values)
            connection.commit()
            values.clear()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    cursor.execute("SET UNIQUE_CHECKS = 1;")
    connection.commit()
    connection.close()

# print("start insert_user", flush=True)
# print(datetime.datetime.now(), flush=True)
# insert_user()
# print("end insert_user", flush=True)
# print(datetime.datetime.now(), flush=True)

# print("start insert_follow", flush=True)
# print(datetime.datetime.now(), flush=True)
# insert_follow()
# print("end insert_follow", flush=True)
# print(datetime.datetime.now(), flush=True)

# print("start insert_post", flush=True)
# print(datetime.datetime.now(), flush=True)
# insert_post()
# print("end insert_post", flush=True)
# print(datetime.datetime.now(), flush=True)

print("start insert_postLike", flush=True)
print(datetime.datetime.now(), flush=True)
insert_postLike()
print("end insert_postLike", flush=True)
print(datetime.datetime.now(), flush=True)


print("start insert_postImgUrl", flush=True)
print(datetime.datetime.now(), flush=True)
insert_postImgUrl()
print("end insert_postImgUrl", flush=True)
print(datetime.datetime.now(), flush=True)


print("start insert_comment", flush=True)
print(datetime.datetime.now(), flush=True)
insert_comment()
print("end insert_comment", flush=True)
print(datetime.datetime.now(), flush=True)


print("start insert_commentLike", flush=True)
print(datetime.datetime.now(), flush=True)
insert_commentLike()
print("end insert_commentLike", flush=True)
print(datetime.datetime.now(), flush=True)
