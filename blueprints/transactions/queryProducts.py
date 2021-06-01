from config import *


def query_products(sql, barcodes, rows):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        cur.execute(sql)
        res = cur.fetchall()

        result = []
        for i in res:
            result.append(i[0])

        cur.close()

        need_to_add = []
        temp = []
        row_tuple = []
        qty = []
        customers = []

        for r in rows:
            customerT = (r[8], r[2], r[3], r[4], r[5], r[7],r[9])
            qtyT = (r[10], r[11])
            rowT = (r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[10], r[11], r[12], r[13], r[17], r[17], r[11])
            row_tuple.append(rowT)
            qty.append(qtyT)
            customers.append(customerT)
            if r[11] not in result and r[11] not in temp:
                temp.append(r[11])
                querySet = (r[11], r[12], r[17])
                need_to_add.append(querySet)

        insert_new_products(need_to_add)
        insert_transactions(row_tuple)
        update_inventory(qty)
        update_customers(customers)


    except Exception as e:
        raise e


def insert_new_products(data):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        sql = "insert into products (barcode, product_name, Qty,cost_price) values(%s,%s,0,%s)"
        cur.executemany(sql, data)
        db.commit()
        cur.close()

    except Exception as e:
        raise e


def insert_transactions(rows):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        sql = "insert into transactions (customer_name, add1, add2, add3, add4, postcode, email, qty, barcode, " \
              "products_name, bag_size, selling_price, profits)" \
              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, " \
              "%s - (select cost_price " \
              "from products " \
              "where barcode=%s" \
              "))"
        cur.executemany(sql, rows)
        db.commit()
        cur.close()

    except Exception as e:
        raise e


def update_inventory(rows):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        sql = "UPDATE products SET Qty=Qty-%s WHERE barcode=%s"
        cur.executemany(sql, rows)
        db.commit()
        cur.close()

    except Exception as e:
        raise e


def update_customers(customers):
    try:
        cur = db.cursor()
        db.ping(reconnect=True)
        sql = "INSERT INTO customers(email, name, Address1, Address2, Address3, postcode, phoneNum) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s)" \
              "ON DUPLICATE KEY UPDATE num_orders=num_orders+1"
        cur.executemany(sql, customers)
        db.commit()
        cur.close()

    except Exception as e:
        raise e

