from config import *


def get_init_data():
    sales=0
    orders=0
    profits=0
    temp_sales=get_total_sales()[0]
    temp_orders=get_total_num_of_orders()[0]
    temp_profits=get_total_profit()[0]
    if temp_sales is not None:
       sales = int(temp_sales)
    if temp_profits is not None:
        orders=int(temp_profits)
    if temp_orders is not None:
        profits= int(temp_orders)



    data = {"sales": sales, "orders": orders, "profits": profits, "customers": 0}
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
    """TODO:
    """
    return
