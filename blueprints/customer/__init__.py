# from flask import Flask, render_template
from flask import *

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customer',methods=['GET','POST'])
def customer():
    pass
    # return render_template('customer.html',pageName="customer")