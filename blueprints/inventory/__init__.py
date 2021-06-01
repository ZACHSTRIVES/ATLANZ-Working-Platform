import xlrd
from flask import *
from .products import *
from .queryInventory import *

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
        return render_template('editInventory.htmil', products=products, user=user)
    elif request.method == 'POST':
        product_name = request.form.get('product_name')
        Qty = request.form.get('Qty')
        cost_price = request.form.get('cost_price')
        sql = "UPDATE products " \
              "SET product_name='%s',Qty=%s,cost_price=%s" \
              " WHERE barcode='%s'" % (product_name, Qty, cost_price, barcode)
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
        sql = "INSERT INTO products (barcode, product_name, Qty, cost_price) " \
              " VALUES ('%s', '%s', %s, %s);" % (barcode, product_name, Qty, cost_price)
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


@inventory_bp.route('/inventory/upload', methods=['GET'])
def uploadInventory():
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))

    return render_template("uploadInventory.html", user=user, pageName="inventory")


@inventory_bp.route('/inventory/upload/execl', methods=['POST'])
def uploadExcel():
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    file = request.files['file']
    f = file.read()  # 文件内容
    data = xlrd.open_workbook(file_contents=f)
    table = data.sheets()[0]
    names = data.sheet_names()  # 返回book中所有工作表的名字
    nrows = table.nrows  # 获取该sheet中的有效行数
    ncols = table.ncols  # 获取该sheet中的有效列数
    if ncols != 90:
        flash("Please check the format of the uploaded file！")

    rows = []

    for i in range(1, nrows):
        row = table.row_values(i)
        rowT = (row[0], row[1], row[2], row[3])

        rows.append(rowT)
    print(rows)

    queryInventory(rows)

    return redirect(url_for("inventory.inventory"))
