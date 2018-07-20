from flask import Blueprint, render_template, request
from src.models.stores.store import Store

store_blueprint = Blueprint("stores", __name__)

@store_blueprint.route("/")
def index():
    stores = Store.all()

    return render_template('stores/store_index.html', stores=stores)

@store_blueprint.route("/store/<string:store_id>")
def store_page(store_id):
    return render_template('stores/store.html', store=Store.get_by_id(store_id))

@store_blueprint.route("/edit/<string:store_id>", methods=['GET', 'POST'])
def edit_store(store_id):
    if request.method == "POST":
        pass
    return "edit store page"

@store_blueprint.route("/delete/<string:store_id>")
def delete_store(store_id):
    return "delete store page"

@store_blueprint.route("/create", methods=["POST", "GET"])
def create_store():
    if request.method == "POST":
        pass
    return render_template('stores/create_store.html')
