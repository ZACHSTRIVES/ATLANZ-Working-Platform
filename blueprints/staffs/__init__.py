from flask import *

staffs_bp = Blueprint('staffs', __name__)


@staffs_bp.route('/staffs', methods=['GET', 'POST'])
def staffs():
    if request.method == 'GET':
        return render_template('staffs.html',pageName="staffs")
