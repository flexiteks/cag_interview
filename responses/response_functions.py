from constants.core.constants import *

################################################
#     Successful Payload Return Functions      #
################################################

def _successful_response(payload, code):
    return payload, code

def _successful_inventory_response(payload, code):
    payload = {ID: payload}
    return _successful_response(payload, code)

def _successful_inventory_timeframe_response(items,total_price, code):
    payload = {ITEMS: items,
               TOTAL_PRICE: total_price}
    return _successful_response(payload, code)

def _successful_aggregate_by_category_response(items,code):
    payload = {ITEMS: items}
    return _successful_response(payload, code)
################################################
#     Error Payload Return Functions      #
################################################

def _error_response(message, code):
    return {MESSAGE: message}, code

###################
# GET: Status 200 #
###################

def successful_inventory_insert_response(val):
    return _successful_inventory_response(val, POST_SUCCESSFUL_RESPONSE_CODE_200)


def successful_inventory_update_response(val):
    return _successful_inventory_response(val, POST_SUCCESSFUL_RESPONSE_CODE_200)

def inventory_timeframe_response(items, total_price):
    return _successful_inventory_timeframe_response(items, total_price, POST_SUCCESSFUL_RESPONSE_CODE_200)


def aggregate_by_category_response(items):
    return _successful_aggregate_by_category_response(items, POST_SUCCESSFUL_RESPONSE_CODE_200)
###########################
# Bad Request: Status 400 #
###########################
def _bad_request_status_400_error(payload):
    return _error_response(payload, code=POST_ERROR_RESPONSE_CODE_400)

