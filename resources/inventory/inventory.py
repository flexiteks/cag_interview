from flask import request
from flask_restful import Resource 
from sqlalchemy.exc import OperationalError

from models.inventory import InventoryItem
from decimal import Decimal
from datetime import datetime

from responses.response_functions import successful_inventory_insert_response, _bad_request_status_400_error, successful_inventory_update_response, inventory_timeframe_response, aggregate_by_category_response

#Task 1
class InsertOrUpdateItem(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            name = request_data.get('name')
            category = request_data.get('category')
            price = Decimal(request_data.get('price'))
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            existing_item = InventoryItem.find_by_name(name)
            
            if existing_item:
                InventoryItem.update_inventory_log(name,category,price,current_time)
                return successful_inventory_update_response(existing_item.id)
            else:
                new_item = InventoryItem.insert_inventory_log(name,category,price)
                return successful_inventory_insert_response(new_item.id)
        except AttributeError as e:
            print(e)
            return _bad_request_status_400_error(e)
        
#Task 2
class InventoryInDateRange(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            dt_from = datetime.strptime(request_data['dt_from'], '%Y-%m-%d %H:%M:%S')
            dt_to = datetime.strptime(request_data['dt_to'], '%Y-%m-%d %H:%M:%S')

            # Query items within the specified date range
            items_in_range = InventoryItem.get_inventory_in_date_range(dt_from, dt_to)

            # Calculate the total price
            total_price = sum(item.price for item in items_in_range)

            return inventory_timeframe_response([item.to_dict() for item in items_in_range], str(total_price))
        except Exception as e:
            return _bad_request_status_400_error(e)

#Task 3
class InventoryAggregatedByCategory(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            category = request_data.get('category')

            # Aggregate items using the class method
            items_aggregated = InventoryItem.aggregate_by_category(category)

            return aggregate_by_category_response([{
                    'category': item.category,
                    'total_price': str(item.total_price),
                    'count': item.count
                } for item in items_aggregated])
        
        except Exception as e:
            return _bad_request_status_400_error(e)