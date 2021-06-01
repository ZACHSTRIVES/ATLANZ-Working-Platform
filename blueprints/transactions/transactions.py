from config import db


def list_all_transactions():
    try:
        cur = db.cursor()
        sql = "select * from transactions order by transactions_id"
        db.ping(reconnect=True)
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()
        cur.close()
        return result

    except Exception as e:
        print(e)

def get_transactions(transactions_id):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        sql = "SELECT * FROM transactions WHERE transactions_id='%s' " % transactions_id
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