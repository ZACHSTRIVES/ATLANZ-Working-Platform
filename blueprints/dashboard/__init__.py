from flask import *
from .getData import *

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    user = session.get("user")
    if user is None:
        return redirect(url_for("auth.login"))
    data = get_init_data()

    return render_template('dashboard.html', pageName="dashboard", user=user, data=data)
