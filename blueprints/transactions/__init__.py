from flask import *
from config import *
from .queryProducts import *
from .transactions import *
import xlrd

transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.route('/transactions', methods=['GET'])
def transactions():
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    if request.method == 'GET':
        transactions = list_all_transactions()
        return render_template("transactions.html", user=user, transactions=transactions, pageName="transactions")


@transactions_bp.route('/transactions/upload', methods=['GET'])
def uploadTransactions():
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))

    return render_template("uploadTransactions.html", user=user, pageName="transactions")


@transactions_bp.route('/transactions/upload/execl', methods=['POST'])
def uploadExcel():
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    file = request.files['file']
    f = file.read()  # 文件内容
    data = xlrd.open_workbook(file_contents=f)
    table = data.sheets()[0]
    names = data.sheet_names()  # 返回book中所有工作表的名字
    status = data.sheet_loaded(names[0])  # 检查sheet1是否导入完
    print(status)
    nrows = table.nrows  # 获取该sheet中的有效行数
    ncols = table.ncols  # 获取该sheet中的有效列数
    if ncols != 90:
        flash("Please check the format of the uploaded file！")

    rows = []

    barcodes = []
    for i in range(1, nrows):
        row = table.row_values(i)
        rows.append(row)
        barcodes.append(row[11])


    query_sql = "SELECT barcode FROM products WHERE barcode IN ( '" + "', '".join(barcodes) + "')"  # 生成sql语句
    query_products(query_sql, barcodes, rows)

    return redirect(url_for("transactions.transactions"))

@transactions_bp.route('/edit_transactions<transactions_id>', methods=['GET', 'POST', 'PUT'])
def edit_transactions(transactions_id):
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    if request.method == 'GET':
        transactions = get_transactions(transactions_id)
        return render_template('edittransactions.html', transactions=transactions, user=user)
    elif request.method == 'POST':
        customer_name = request.form.get('customer_name')
        email = request.form.get('email')
        qty = request.form.get('qty')
        products_name = request.form.get('products_name')
        bag_size = request.form.get('bag_size')
        selling_price = request.form.get('selling_price')
        profits = request.form.get('profits')
        sql = "UPDATE transactions " \
              "SET customer_name='%s',email='%s', qty=%s, products_name='%s', bag_size=%s, selling_price=%s, profits=%s" \
              " WHERE transactions_id='%s'" % (customer_name,email, qty, products_name, bag_size, selling_price, profits, transactions_id)
        change_transactions_db(sql)

        return redirect(url_for("transactions.transactions"))

@transactions_bp.route('/del_transactions<transactions_id>', methods=['GET', 'DELETE'])
def del_transactions(transactions_id):
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    sql = "delete from transactions where transactions_id='%s'" % transactions_id
    change_transactions_db(sql)

    return redirect(url_for("transactions.transactions"))