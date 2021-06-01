from flask import *
from config import *
from .queryProducts import *
import xlrd

transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.route('/transactions', methods=['GET'])
def transactions():
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    if request.method == 'GET':
        return render_template("transactions.html", user=user, pageName="transactions")


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
