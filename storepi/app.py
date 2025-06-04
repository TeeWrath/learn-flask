import uuid
from flask import Flask, request
from db import items,stores
from flask_smorest import abort
app = Flask(__name__)

@app.get("/store")
def get_stores():
    return {"stores" : list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad request. Ensure 'name' is included in the JSON payload. ")
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400,message="store already exists. ")
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id" : store_id}
    stores[store_id] = new_store
    return new_store,201

@app.get("/store/<string>:store_id")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "store not found"},404
    
@app.post("/item")
def create_item():
    item_data = request.get_json()
    if(
        "price" not in item_data or "store_id" not in item_data or "name" not in item_data
    ): abort(
        400,
        message="Bad request. Ensure 'price', 'store_id' and 'name' are included in the JSON payload."
    )
    for item in items.values():
        if(
            item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]
        ): abort(400, message=f"item {item_data} already exists")
    if item_data["store_id"] not in stores:
        abort(404 , message="store not found")
    item_id = uuid.uuid4().hex
    item = {**item_data, "id" : item_id}
    items[item_id] = item
    
    return item,201

@app.get("/item/<string>:item_id")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message" : "item not found"},404
    
@app.delete("/item/<string>:item_id")
def delete_an_item(item_id):
    try:
        del items[item_id]
        return {"message":"Item deleted"},200
    except KeyError:
        abort(404,message="Item not found.")

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]},201
    return {"message": "store not found"},404