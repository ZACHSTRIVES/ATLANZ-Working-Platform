from config import db


def list_all_staffs():
    try:
        cur = db.cursor()
        sql = "select * from users order by name"
        db.ping(reconnect=True)
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()
        cur.close()
        return result

    except Exception as e:
        print(e)

def get_staffs(name):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        sql = "SELECT * FROM users WHERE name='%s' " % name
        cur.execute(sql)
        result = cur.fetchone()
        db.commit()
        cur.close()
        return result
    except Exception as e:
        print(e)


def change_transactions_db(sql):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()
        cur.close()
        return result

    except Exception as e:
        print(e)