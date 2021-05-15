from flask import *

marketing_bp = Blueprint('marketing', __name__)

@marketing_bp.route('/marketing',methods=['GET','POST'])
def marketing():
    pass
    # return render_template('marketing.html')