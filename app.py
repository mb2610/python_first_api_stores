from email import message
import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

app = Flask(__name__)

######################################################

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_stores():
    store_data = request.get_json()
    
    if "name" not in store_data:
        abort(400, "Bad request. Ensure 'name' is included int the JSON payload.")
    
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message="Store already exists.")

    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores.append(new_store)
    return new_store, 201

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")

######################################################

@app.post("/item")
def create_item():
    item_data = request.get_json()
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(400, "Bad request. Ensure 'price', 'store_id' and 'anem' are included int the JSON payload.")
    
    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message="Item already exists.")

    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")

    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}    
    stores.append(new_item)
    return new_item
      
@app.get("/item")
def get_all_item():
    return {"items": list(items.values())}

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")
