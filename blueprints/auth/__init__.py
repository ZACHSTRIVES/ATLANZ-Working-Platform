from flask import *

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('page-login.html')
