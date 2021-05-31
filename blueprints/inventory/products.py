from config import db

def list_all_products():
    try:
        cur = db.cursor()
        sql = "select * from products"
        db.ping(reconnect=True)
        cur.execute(sql)
        result = cur.fetchall()
        return result

    except Exception as e:
        print(e)

def get_products(barcode):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        sql = 'SELECT * FROM products WHERE barcode=%s' % barcode
        cur.execute(sql)
        result = cur.fetchone()
        return result
    except Exception as e:
        print(e)

def change_product_db(sql):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()
        return result

    except Exception as e:
        print(e)