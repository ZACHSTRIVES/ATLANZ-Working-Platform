from config import db


def queryInventory(rows):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        sql = "INSERT INTO products(barcode, product_name, Qty, cost_price) " \
              "VALUES (%s,%s,%s,%s) " \
              "ON DUPLICATE KEY UPDATE " \
              "product_name=VALUES(product_name),Qty=Qty+VALUES(Qty),cost_price=VALUES(cost_price)"
        cur.executemany(sql, rows)
        db.commit()
        cur.close()

    except Exception as e:
        raise e
