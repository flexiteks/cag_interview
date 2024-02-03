from flask import Flask, request, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
import json

from imports import db

from dotenv import load_dotenv

from resources.inventory.inventory import InsertOrUpdateItem, InventoryInDateRange, InventoryAggregatedByCategory

from constants.core.environment_variables import debug_mode

load_dotenv()

########################################
#     Define the Flask application     #
########################################
app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response

app.config.from_object('config.Config')
app.config.from_object('config.ProdConfig')
app.config.from_object('config.DevConfig')
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
###################################################################################

####################################################################
#     Routing of Resources to endpoints for the Inventory API     #
####################################################################

# 1.1)  Inserting or updating inventory
api.add_resource(InsertOrUpdateItem, '/api/insert-update-inventory')

# 1.2)  Get Inventory within timeframe
api.add_resource(InventoryInDateRange, '/api/get-inventory-in-timeframe')

# 1.3)  Aggregate Inventory by Category
api.add_resource(InventoryAggregatedByCategory, '/api/aggregate-inventory')


#######################################################
#    Create application, databases and all tables     #
#######################################################
jwt = JWTManager(app)
CORS(app)

db.init_app(app)

@ app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=debug_mode, port=5000)