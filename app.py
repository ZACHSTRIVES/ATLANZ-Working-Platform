from flask import *

from blueprints import auth,staffs,dashboard,customer,transactions,inventory


import config

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(auth.auth_bp)
app.register_blueprint(dashboard.dashboard_bp)
app.register_blueprint(staffs.staffs_bp)
app.register_blueprint(inventory.inventory_bp)
app.register_blueprint(transactions.transactions_bp)



if __name__ == '__main__':
    app.run()
