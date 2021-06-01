from config import *


def get_init_data():
    sales = int(get_total_sales()[0])
    orders = int(get_total_num_of_orders()[0])
    profits = int(get_total_profit()[0])


    customers=0
    customersTemp=get_total_customers()[0]
    if customersTemp is not None:
        customers=int(customersTemp)
    data = {"sales": sales, "orders": orders, "profits": profits, "customers": customers}
    return data


def get_total_sales():
    try:
        cur = db.cursor()
        sql = "select sum(selling_price) from transactions"
        db.ping(reconnect=True)
        cur.execute(sql)
        result = cur.fetchone()
        return result

    except Exception as e:
        print(e)


def get_total_num_of_orders():
    try:
        cur = db.cursor()
        sql = "select count(barcode) from transactions"
        db.ping(reconnect=True)
        cur.execute(sql)
        result = cur.fetchone()
        return result

    except Exception as e:
        print(e)


def get_total_profit():
    try:
        cur = db.cursor()
        sql = "select sum(profits) from transactions"
        db.ping(reconnect=True)
        cur.execute(sql)
        result = cur.fetchone()
        return result

    except Exception as e:
        print(e)


def get_total_customers():
    try:
        cur = db.cursor()
        sql = "select count(*) from customers"
        db.ping(reconnect=True)
        cur.execute(sql)
        result = cur.fetchone()
        return result

    except Exception as e:
        print(e)
    return


