from flask import *

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard',methods=['GET','POST'])
def dashboard():

    return render_template('dashboard.html',pageName="dashboard")