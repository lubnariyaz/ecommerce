from app import app
from flask import request, send_file
from model.product_model import product_model
from datetime import datetime

obj = product_model()

@app.route("/product/viewall")
def product_viewall_controller():
    return obj.product_viewall_model()

@app.route("/product/addone", methods=["POST"])
def product_addone_controller():
    return obj.product_addone_model(request.form)

@app.route("/product/update", methods=["PUT"])
def product_update_controller():
    return obj.product_update_model(request.form)

@app.route("/product/delete/<id>", methods=["DELETE"])
def product_delete_controller(id):
    return obj.product_delete_model(id)