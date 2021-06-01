from flask import *
from config import db
from .staffs import *

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


@staffs_bp.route('/add_staffs', methods=['POST', 'PUT'])
def add_staff():
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


@staffs_bp.route('/edit_staffs<name>', methods=['GET', 'POST', 'PUT'])
def edit_staffs(name):
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    if request.method == 'GET':
        staffs = get_staffs(name)
        return render_template('edit_staffs.html', staffs=staffs, user=user)
    elif request.method == 'POST':
        password = request.form.get('password')
        type = request.form.get('type')
        sql = "UPDATE users " \
              "SET password='%s', type=%s" \
              " WHERE name='%s'" % (password, type, name)
        change_transactions_db(sql)

        return redirect(url_for("staffs.staffs"))

@staffs_bp.route('/del_staffs<name>', methods=['GET', 'DELETE'])
def del_staffs(name):
    try:
        cur = db.cursor()
        sql = "delete from users where name='%s'" % name
        db.ping(reconnect=True)
        cur.execute(sql)
        db.commit()
        cur.close()
    except Exception as e:
        raise e
    return redirect(url_for("staffs.staffs"))