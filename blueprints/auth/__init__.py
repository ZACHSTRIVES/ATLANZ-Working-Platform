from flask import *
from config import *

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
def loginPage():
    user = session.get("user")
    if user is not None:
        return redirect(url_for("dashboard.dashboard"))
    if request.method == 'GET':
        return render_template('page-login.html')


@auth_bp.route('/login', methods=['GET'])
def get_login():
    user = session.get("user")
    if user is not None:
        return redirect(url_for("dashboard.dashboard"))
    if request.method == 'GET':
        return render_template('page-login.html')


@auth_bp.route('/login', methods=['POST'])
def login():
    name = request.form.get("name")
    password = request.form.get("password")
    try:
        cur = db.cursor()
        sql = "SELECT * FROM users WHERE name='%s'" % name
        db.ping(reconnect=True)
        cur.execute(sql)
        cur.close()
        result = cur.fetchone()
        if result is None:
            flash("User does not exist！")
            return render_template("page-login.html")

        else:
            if password != result[1]:
                flash("Wrong Password!")
            else:
                session["user"] = result
                return redirect(url_for("dashboard.dashboard"))


    except Exception as e:
        raise e


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for(('auth.login')))


