from flask import *
from blueprints.inventory.products import *

inventory_bp = Blueprint('inventory', __name__)


@inventory_bp.route('/inventory', methods=['GET', 'POST'])
def inventory():
    # login_ = login_status()
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    if request.method == 'GET':
        products = list_all_products()
        return render_template('inventory.html', products=products, user=user)


@inventory_bp.route('/edit_products<barcode>', methods=['GET', 'POST', 'PUT'])
def edit_products(barcode):
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    if request.method == 'GET':
        products = get_products(barcode)
        return render_template('editInventory.html', products=products, user=user)
    elif request.method == 'POST':
        product_name = request.form.get('product_name')
        Qty = request.form.get('Qty')
        cost_price = request.form.get('cost_price')
        selling_price = request.form.get('selling_price')
        sql = "UPDATE products " \
              "SET product_name='%s',Qty=%s,cost_price=%s,selling_price=%s" \
              " WHERE barcode='%s'" % (product_name, Qty, cost_price, selling_price, barcode)
        change_product_db(sql)

        return redirect(url_for("inventory.inventory"))


@inventory_bp.route('/add_products', methods=['GET', 'POST', 'PUT'])
def add_products():
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    if request.method == 'GET':
        return render_template('addInventory.html', user=user)
    elif request.method == 'POST':
        barcode = request.form.get('barcode')
        product_name = request.form.get('product_name')
        Qty = request.form.get('Qty')
        cost_price = request.form.get('cost_price')
        selling_price = request.form.get('selling_price')
        sql = "INSERT INTO products (barcode, product_name, Qty, cost_price, selling_price) " \
              " VALUES ('%s', '%s', %s, %s, %s);" % (barcode, product_name, Qty, cost_price, selling_price)
        change_product_db(sql)


        return redirect(url_for("inventory.inventory"))


@inventory_bp.route('/delproducts<barcode>', methods=['GET', 'DELETE'])
def del_product(barcode):
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    sql = "delete from products where barcode='%s'" % barcode
    change_product_db(sql)
    return redirect(url_for("inventory.inventory"))
