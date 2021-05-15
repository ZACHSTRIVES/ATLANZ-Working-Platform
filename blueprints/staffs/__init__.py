from flask import *
from config import db

staffs_bp = Blueprint('staffs', __name__)


@staffs_bp.route('/staffs', methods=['GET', 'POST'])
def staffs():
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    if request.method == 'GET':
        try:
            cur = db.cursor()
            sql = "SELECT * FROM users"
            db.ping(reconnect=True)
            cur.execute(sql)

            db.commit()
            cur.close()
            result = cur.fetchall()
        except Exception as e:
            raise e

        return render_template('staffs.html', pageName="staffs", staffs=result,user=user)


@staffs_bp.route('/edit_staffs', methods=['POST', 'PUT'])
def edit_staff():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        type = request.form.get('type')
        try:
            cur = db.cursor()
            sql = "INSERT INTO users (name, password, type) VALUES ('%s','%s',%s)" % (name, password, type)
            db.ping(reconnect=True)
            cur.execute(sql)
            db.commit()
            cur.close()
            return redirect(url_for("staffs.staffs"))
        except Exception as e:
            raise e

    elif request.method == 'PUT':
        return
