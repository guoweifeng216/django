import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                        user='root',
                        password='zxcv.0123',
                        db='test',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

try:
        with connection.cursor() as cursor:
        # Create a new record
            sql = 'INSERT INTO guest (realname, phone, email, sign, event_id,' \
                  'create_time) VALUES ("alen",18800110001,"alen@mail.com",0,1,NOW());'

            cursor.execute(sql)

        connection.commit()

        with connection.cursor() as cursor:
        # Read a single record
            sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
            cursor.execute(sql, ('18800110001',))
            result = cursor.fetchone()
            print(result)
finally:
        connection.close()