from flask import *

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'GET':
        return render_template('page-login.html')

@auth_bp.route('/login',methods=['POST'])
def login():

    return redirect(url_for("dashboard.dashboard"))
