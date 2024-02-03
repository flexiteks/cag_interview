import requests
import json

# Define the base URL
base_url = 'http://127.0.0.1:5000'

# TASK #1: Insert or Update Inventory Item
insert_update_url = f'{base_url}/api/insert-update-inventory'
insert_update_data = {
    'name': 'Notebook',
    'category': 'Stationary',
    'price': '5.5'
}
response_insert_update = requests.post(insert_update_url, json=insert_update_data)
print('\n\nTask1:\nInsert or Update Response:', response_insert_update.status_code)
print(json.dumps(response_insert_update.json(), indent=2))

# TASK #2: Get Inventory in Timeframe
get_inventory_url = f'{base_url}/api/get-inventory-in-timeframe'
get_inventory_data = {
    'dt_from': '2022-01-01 10:00:00',
    'dt_to': '2025-01-25 10:00:00'
}
response_get_inventory = requests.post(get_inventory_url, json=get_inventory_data)
print('\n\nTask2:\nGet Inventory Response:', response_get_inventory.status_code)
print(json.dumps(response_get_inventory.json(), indent=2))

# TASK #3: Aggregate Inventory by Category
aggregate_inventory_url = f'{base_url}/api/aggregate-inventory'
aggregate_inventory_data = {
    'category': 'all'
}
response_aggregate_inventory = requests.post(aggregate_inventory_url, json=aggregate_inventory_data)
print('\n\nTask3:\nAggregate Inventory Response:', response_aggregate_inventory.status_code)
print(json.dumps(response_aggregate_inventory.json(), indent=2))