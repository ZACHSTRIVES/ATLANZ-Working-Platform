from flask import *


app = Flask(__name__)

@app.route('/')
def hello():

    return render_template("page-login.html")